PRACTICE 2 - REVISION 1    
# WORLD EVENT CURATION PLOT SYSTEM


## CONTACT INFORMATION: 
Paola González Hernández - <paaoogh@gmail.com>  

## DISCLAIMER:
This project, alongside its content and multimedia used in the Wordpress blog, is protected under the copyleft GNU General Public License of 2007. 

## INTRODUCTION: Overview
The Earth is experimenting diverse natural episodes through time. Now at days, technology allows us to track them in (almost) live stream. The National Aeronatics and Space Administration (NASA) has devoted part of their investigation to work with natural events curation, they have developed a project named EONET (Earth Observatory Natural Event Tracker), and colaborating with the Earth Observatory and the ESDIS project (Earth Science Data and Information System), they have acheived the conversion of satellite imaginery into metadata.  

Even though the definition of what a natural event is could be intuitive, the lack of consistency brings new contraints that includes (but is not limited to): contextual parameters, the meaning of different definitions proportioned by diverse sources to an end urser, and the interpretation that both peers may give them.  

This project aims to make a distributed system that helps the understanding of the above mentioned and reducing the contextual conflict by showing plottings and retreiving NASA open data within a period of time; the plottings are a description of the magnitude of a natual event. The need of generating a product that will allow the public in general to understand the files comes from the fact that not all the people around the globe know that a JSON (JavaScript Object Notation) file is and, what is more, how to interpret it. 

As the amount of information retreived from the EONET API is bigger than what a simple and individual program could handle, a set of components (modules) are the ones in charge of every piece of a major process that describe this project. Different physical components are needed in case you want to download this project: the data source will provide the metadata, but the storaging system in a database with SQL language is mandatory; afterwards, data has to be processed and delivered at a final application (Wordpress blog in this case). Although just one system is mentioned for the processing, this project also uses another server in order tu generate the place where the images (final plottings) are taken from in Wordpress. Furthermore: this EONET distributed computing system has a client-server architechture. 

### Techniques and Methodology
**General idea:**Following the eXtreme Programming schema, the NASA EONET will be the data provider that will allow the personal computer to send the data to a server. The final client will be able to get the data needed in the form of diverse graphs.  

Tools needed:
* *Primary programming language:* Python 3.x
* *Python primary libraries:* json, requests, sys, subprocess, mysql connector,  
* *Other Python libraries:*  matplotlib, glob, datetime, shutil, wget
* *Database Management System:* MySQL 
* *Other software tools:* JSON files, Visual Studio Code, networking protocols 
* *Other physical tools:* external server

*Important: this project has been developed with Linux Operative System. Some processes may work differently with Windows or MacOS Catalina version.*

**General description of the architecture**

The curated data acquired from the EONET page has been already processed by the NASA Earth Observatory and the ESDIS, the geographical imaginery come from their satellite. Metadata will take time to get to the personal computer as the information travels through the internet: before entering to the local network, the packets have to go through a router and again through the firewall that connects to the server. 

The diagram bellow illustrates the process in a more detailed manner.

**How did the eXtreme Programming has to work here?**

The idea is manage this project with agile methods that will allow any changes to be implemented with enought time. The integrants of the former team had to understand every component and the way in which they are related as a whole. It is important, though, if collaboration or cloning of this project is desired, to also take time to understand the processes at the programs and the architecture of the database used, so as the original organization of the files that will be mentioned bellow. 

## SOFTWARE REQUIREMENTS AND INSTALLATION:
In the aim of control the data access, NASA need to generate the proper developer credentials. The can be requested [here](https://api.nasa.gov). The limited downloading of data per hour and IP address within different APIs is available with a demo key. For the moment, NASA EONET is not requiring APIs credential, but may be requested in further processes as requested from de NASA.

Having the software tools mentioned above will make easier the process. It is also necessary, in case cloning the project is the desire, to install git and configure it with your account through:

```
$ sudo apt-get update
$ sudo apt-install git

#Verify the installation was successfull:
$ git --version
>> git version 2.9.2

#Configure username and email:
$ git config --global user.name "My User"
$ git config --global user.email "myuser@example.com"
```
And through a `git clone https://github.com/paaoogh/Distributed_Computing_ENES-UNAM.git` on the terminal/command line you will get a local copy of this repository.

In case you want to see the site used for this project, redirect yourself to the Wordpress Blog [EONET Plotting](eonetplotting.wordpress.com)

## IMPLEMENTATION: HANDLING DATA

*Important: the current EONET metadata version moved from 2.1 to 3, although the first one is still available, I am working with version 3.* 

Downloadable APIs include: Events (which is the main data for this project - GeoJson), Categories and Layers. A further description of the data types and the meaning of what is downloaded is depicted in this [source](https://eonet.sci.gsfc.nasa.gov/docs/v3). If downloaded directly into personal computer, a single file without any extension will be stored; in case you want to save it as .JSON, it will have to be added manually. 

### Data description:

**Introduction to the contextual formating:** NASA EONET project works with a contextual format called "GeoJSON" that workis tith the World Geodetic System of 1984. This is an information interchange format for geospacial data for different types fo JSON files that include diverse manners to represent geographical features such as properties and geometry (type of point and coordinates). GeoJSON Status definition can be found in the [RFC 2026](https://www.rfc-editor.org/info/rfc2026) and the definition of Stream at [RFC 4844](https://rfc-editor.org/info/rfc4844).

JSON files are easier to manage when storagin into a database because they have a "hash-table-structure-Python-dictionary" alike format. This allows to simply convert the keys into attributes and the values as entries; in other other words: JSON files are easier to parse. 

**Data downloaded from EONET**

In first instance, a single file is downloaded from the API, you can see in the section *"Data retrieving and storaging* how the process works with the program *01_retrieving.py*; the main point to mention here is that not all the features that EONET provides are used. The following chart can illustrate the data that I am working with:

| **FIELD** |**DESCRIPTION**|**MANDATORY**|**EXAMPLE**|**DATABASE TABLE**|**DATABASE ALIAS**|
|--------|-----------|---------|-------|--------------|--------------|
|**ID_EVENT** | Unique ID for these events | YES | EONET_354 | events | ID |
|**NAME_EVENT** | Title of the event |YES | Dukono Volcano, Indonesia | events | TITLE|
|**DESCRIPTION** | Optional longer description of the event made of a couple of sentences | NO | During 16 and 19-22 March, ash plumes from Dukono rose to altitudes of 1.5-2.4 km (5,000-8,000 ft). | events | DESCRIPTION |
|**ID_GEOMETRY** | Unique ID of measurements made per event | YES | 1_EONET_354 | geometry | ID_GEOM |
|**MAGNITUDE** | Information about magnitude of each event displayed if available | NO |35.0 | geometry | MAGNITUDE |
|**UNITS** | Units of measurements for magnitudes if available | NO | kts | geometry | UNIT |
|**GEOMETRY** | Type of mark per event | YES | point | geometry | TYPE |
|**DATES**| Date of occurrence per event | YES | 2020-08-01T18:000:00Z | geometry | DATE |

Also, it you wish, there is a directory called ["
Complementary material](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/tree/master/
complementary%20material) where you can find examples of the files created, MySQL more explicit tables and diagrams, and the final plottings (that are the aim of this project).

### Data retrieving and storaging:


### Processing data:

### Further processes

### Working on a web page


## TESTING AND ANALYZING

## CONCLUSIONS:
   1. It is very important to get to know and understand the data that you are working with in order to proceed to diverse steps. This includes (and is not limited to) understanding the format, data types and restrictions (such as legal protection of data). In this case, the first challenge faced was working and processing with no-extension files, followed by the arrangements of the data provided by EONET.

### EONET as a whole

### EONET in progress

### Bumps and challenges

### A new vision of the world
   
Several stages will allow us to generate comments within this section and will be submited when apropiate.

## BIBLIOGRAPHY AND REFERENCES:
    1. *{NASA APIs}* (NASA Open Innovation Team,2020). Retreived from: <https://api.nasa.gov>. 
    2. *What is EONET?* (EONET et al, 2020). Retreived from: <https://eonet.sci.gsfc.nasa.gov/what-is-eonet>
    3. *Version 3 Documentation* (EONET et al, 2020). Retreived from: <https://eonet.sci.gsfc.nasa.gov/docs/v3>

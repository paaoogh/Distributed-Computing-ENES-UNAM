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

![logic conection](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/blob/master/Diagrams/logic%20conection.png)

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

*Important: the current EONET metadata version moved from 2.1 to 3, although the first one is still available until the end of 2020, I am working with version 3.* 

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

**01_retrieve.py:** through a *request* to the one single file will be obtained without any extension but JSON format.There is a huge listing of reported events up to that specific date that the file is downloaded, each element will be a file with extension .json that willbe stored at the personal computer and the server though scp protocol. 

If you only run this program, make sure you already are within its directory and you will have a copy of every natural event description in a file. Each file will contain many measurements of the event alonside with a  lot of data that, as mentioned above, will not all be used for the moment. It is very important to save correctly the documents as it could make a failure to control de information otherwise.

**02_dbstoring.py:** in this case, the algorithm to follow will be:
- 1. Open a connection to the database.
- 2. Open a cursor.
- 3. Make an abstract query (more or less generic). This this part would be a good idea to try the query by itself on the database before executing the program.
- 4. for each file:
-    1. Open file and parse.
-    2. Extract and cast information.
-    3. List data.
-    4. Execute query over cursor.
-    5. Move file from static to backup with subprocess library.

Another and simpler way to see it is following the path that the information follows: from the satellite and after NASA EONET has curated the metadata, 01_retrieve.py will request through internet the data and split it into .json files. 02_dbstoring.py will move the files into the server and a database:

![Data flux](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/blob/master/Diagrams/Data%20flux.png)


### Processing data:

From the many possibilities of showing plottings, this project decided to use bar graphs as they are more intuitive to end users and easier to understand. *03_processing.py* makes another query (with the same idea of only opening one connector as mentioned above) of selecting the magnitudes and plotting them in a single bar. 

At the beginning, it did not matter if the images produced were overwritten by the program initially named "last flux. png", nonetheless an end user could want to see past events measurements, so now they are named with the dating that they were generated. This will also help the wordpress blog to redirect the webpage to the proper image. 

Also, the final product of this execution, will be copied into the server main static page. 

### Further processes

**04_moving.py:** this is an extra process for interal control at the personal computer where this project is executed. Once the event files are created in the main directory of this project, they will be moved to another place with the execution date in the personal computer so no redundances are made. 

**Further more:**
As a distributed computing project, up to this point, we only got separated threads of processes, now it is important to put them all together into a single masterpiece: *ordering.sh* will be the point guard and point forward of the game. 

Inpired by the Berkeley algorithm with inalambric networking and the Lamport logic clocks, this project works with the idea of following a sequence, more than sincronizing timings and clocks: it will be enough with making the processes to be well-ordered and coordinated without having the computer and server to be exactly sincornized at the "real time"... because, at the end of it: what is even real time? We cannot actually sincronize clocks perfectly (logically and/or phyisically). 

As that being said: the important thing will be exectute *ordering.sh* at a certain time of the personal computer or the server with crontab -e. This script contrains the moving of files and changing of directories needed.

![data processing](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/blob/master/Diagrams/data%20processing.png)

### Working on a web page

As said at the beginning, the plottings will be shown at a [Wordpress Blog](eonetplotting.wordpress.com) where a more coloquial description of the project is provided. This page will redirect to the server static page. In a further increment, using the library of python for wordpress can be implemented for authomatic redirection to a specific image. 

The last point mentioned above brings us to the fact that sharing data can go from something simple as an html page to a more complex project such as web services modules that allow to standarize creation processes of web services, sharng the project and making it easy to install, for example, a plug-in. 

## TESTING AND ANALYZING

Making a distributed computing project is not as easy as it seems: working in a local network as much as possible is makes everything faster and easier but there are limits imposed by the needs of the project itself. In this specific case of EONET plottings, as seen in the diagrams before, we have to go through the internet a couple times, that means that we have to take into consideration security, geographical scopes and **time of information interchange**.

The fact that the routes that packets take may not be the same and that, before getting to any server services, information has to go through regional routers and meganodes routers are one of the main reasons why testing a couple times how long does every process take is very important. With that in mind, further increments and cycles for the project to grow can be applied: you will know how often cant you update the information in order to apply correctly the crontab.

EONET Plottig project has the following timings in average:

![latency](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/blob/master/Diagrams/latency.png)

As said before, there is directory with complementary images of examples of the plottings made, but, in general, they look like this:

![2020-08-08](https://github.com/paaoogh/Distributed-Computing-ENES-UNAM/blob/master/Complementary%20material/PLOTTINGS/2020-08-08.png)

## CONCLUSIONS:

### EONET as a whole
- The data provided by EONET also gives a wide area of growth and many scalability options. The curation of events is a very important part of this project and EONET by itself: the definition of what constitutes an event is still fluid in terms that there is no exact and real definition. A very important question may define the focusing of cloning and contributing to this project: What are the contextual parameters of an event? 
- Working with (almost) real time data is more complex than it sounds. Only focusing of using one single tool and master it woudln't begin to describe this project, that is another reason why ONET Plotting can grow even more. A plug-in can be developed in a not so far future.

### EONET in progress
- Only a couple of cycles (increments) were made up to now. Further processes include crontab and working with a framework such as Mezzanine (taking into consideration the requirements for each operative sistem and versions for each component of the framework and Django). 
- As data is very extense and the data type is not restricted to only a specific type of numbers, other queries can be made and other tables in the database may be added. This will bring the oportunity to not only work with bar plottings, also other areas of data science could be involved, such as time series at certain geographic areas, Machine Learning for clustering analysis, among others.

### Bumps and challenges
- NASA, as said before, is still working with contextualization of events, which sometimes bring the API's downloads to differ. At some point there was a slight change of the definition of the events that was not so easy to debbug in the project. From this, it is important to always get updates of the API's changes if they occur.
- Initially, working with Mezzanine and Django was the goal, but the operative system that I am currently working with did not meet its software requirements. This was found after a long time of researching online, which made the project to migrate into a blog. 
- Being single student working on this project was not easy at all, but also not impossible. Team working can make everything better and easier followin the eXtreme Programming methodology. 
- By the time you read this, maybe we won't be on a world pandemic... but doing home office is not easy, what is more: learning from home a whole new subject is even more difficult.

### A new vision of the world
- With this project, not only distributed computing knoledge was important, but also management of operative systems, a little bit of hardware research and more was gained. 
- Disecting an enourmous critical project into small pieces of components that work along is sometimes easier to implement and understand, mostly if someone else is going to read the project or wants to work with you.
- Sometimes you do not need a book to help you learn, but knowing where to seach and how to do so... This project has been all about learning to learn and loosing the fear to experiment and try new things with my computer. With this I am not encouraging you to mess up you personal computer or, what's even more, your working station; I do am saying that this project made me grow as a data science student by loosing the fear to learn and try new things. 

## BIBLIOGRAPHY AND REFERENCES:
    1. *{NASA APIs}* (NASA Open Innovation Team,2020). Retrieved from: <https://api.nasa.gov>. 
    2. *What is EONET?* (EONET et al, 2020). Retrieved from: <https://eonet.sci.gsfc.nasa.gov/what-is-eonet>
    3. *Version 3 Documentation* (EONET et al, 2020). Retrieved from: <https://eonet.sci.gsfc.nasa.gov/docs/v3>
    4. *The GeoJSON Format* (Butler, H. et all). RFC 7946, DOI 10.17587/RFC7946, August 20016. Retrieved from: <https://www.rfc-editor.org/info/rfc7946>
    5. *WordPress.com: Create a Free Website of Blocg*. (WordPress, 2020). Retrieved from <https://wordpress.com>
    6. *Wordpress API - Python Client*. (Sanchez, C., 2020) Retrieved from: <https://www.github.com/derwentx/wp-api-python>
    

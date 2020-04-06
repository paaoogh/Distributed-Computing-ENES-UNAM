PRACTICE 1 - REVISION 1    
# WORLD EVENT CURATION PLOT SYSTEM


## CONTACT INFORMATION OF CONTRIBUTORS TO THE PROJECT:
Maria Lucrecia Beltz González - <lucreciabeltz@gmail.com>  
Paola González Hernández - <paaoogh@gmail.com>  
Samuel Gomez Lara - <samuelgolara@gmail.com>  

## INTRODUCTION: Overview
The Earth is experimenting diverse natural episodes through time. Now at days, technology allows us to track them in (almost) live stream. The National Aeronatics and Scpace Administration (NASA) has devoted part of their investigation to work with natural events curation, they have developed a project named EONET (Earth Observatory Natural Event Tracker), and colaborating with the Earth Observatory and the ESDIS project (Earth Science Data and Information System), they have acheived the satellite imaginery into metadata.  

Even though the definition of what a natural event is could be intuitive, the lack of consistency brings new contraints that includes (but is not limited to): contextual parameters, the meaning of different definitions proportioned by diverse sources to an end urser, and the interpretation that both peers may give them.  

This project aims to make a distributed system that helps the understanding of the above mentioned by showing graphs and retreiving NASA open data within a period of time.

### Technique and Methodolgy
Following the eXtreme Programming schema, the NASA EONET will be the data provider that will allow the personal computer to send the data to a server. The final client will be able to get the data needed in the form of diverse graphs.  

Tools needed:
    * Python programming language
    * Python libraries: Json, requests, matplotlib, numpy, datetime
    * Json
    * Lighttpd
    * Visual Studio Code
    * Other python libraries will be updated as the project moves forward.

Run the retreive.py program for the data fetching. It will be stored in a .csv file that will be processed later. Conection with the API is stablished within the program.


## REQUIREMENTS:
In the aim of control the data access, NASA need to generate the proper developer credentials. The can be requested [here](https://api.nasa.gov). The limited downloading of data per hour and IP adress within different APIs is available with a demo key. For the moment, NASA EONET is not requiring APIs credential, but may be requested in further processes.

## DATA RETREIVING:
Run the script retreive.py to get the files. Files are not downloaded but processed into Python dictionaries.

The version with which we will be working is version 3, but version 2.1 is still available.  

Downloadable APIs include: Events (which is the main data for this project - GeoJson), Categories and Layers. A further description of the data types and the meaning of what is downloaded is depicted in this [source](https://eonet.sci.gsfc.nasa.gov/docs/v3). If downloaded directly into personal computer, files without any extension will be stored; in case you want to save it as .JSON, it will have to be added manually. 


## CONCLUSIONS:
   1. It is very important to get to know and understand the data that you are working with in order to proceed to diverse steps. This includes (and is not limited to) understanding the format, data types and restrictions (such as legal protection of data). In this case, the first challenge faced was working and processing with no-extension files, followed by the arrangements of the data provided by EONET.
   
Several stages will allow us to generate comments within this section and will be submited when apropiate.

## BIBLIOGRAPHY AND REFERENCES:
    1. *{NASA APIs}* (NASA Open Innovation Team,2020). Retreived from: <https://api.nasa.gov>. 
    2. *What is EONET?* (EONET et al, 2020). Retreived from: <https://eonet.sci.gsfc.nasa.gov/what-is-eonet>
    3. *Version 3 Documentation* (EONET et al, 2020). Retreived from: <https://eonet.sci.gsfc.nasa.gov/docs/v3>

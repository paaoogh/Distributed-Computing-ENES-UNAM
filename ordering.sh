#!/bin/bash

cd $Documents
cd Documents

#direction=$(head -n 1 data.txt)
Environment="PATH=/home/paola/Documents/Distributed-Computing-ENES-UNAM/01_retrieve.py"
echo Creating JSON files at EONET project ... 
python3 Distributed-Computing-ENES-UNAM/01_retrieve.py

Environment="PATH=/home/paola/Documents/Distributed-Computing-ENES-UNAM/02_dbstoring.py"
echo Mounting queries and moving to database...
python3 Distributed-Computing-ENES-UNAM/02_dbstoring.py

Environment="PATH=/home/paola/Documents/Distributed-Computing-ENES-UNAM/03_processing.py"
echo Plotting data...
python3 Distributed-Computing-ENES-UNAM/03_processing.py 

Environment="PATH=/home/paola/Documents/Distributed-Computing-ENES-UNAM/04_moving.py"
echo Moving to new directory files
python3 Distributed-Computing-ENES-UNAM/04_moving.py 

#Cron for automation ans scheduling of the tasks

#When ready, start cron with the following commands

#check cron status:
#systemctl status cron

#To star it:
#systemctl start cron

#minute hour day-month month day-year user command
#00 23 * * * paola sh /ordering.sh
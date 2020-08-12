#!/usr/bin/env python3

#Important libraries at the top. For future usage libraries will be commented with a (*)

import json
import requests
import sys
import subprocess
import os
#--------*-----
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

api = "" #credential
response_events = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events")
data = response_events.json()
PATH="/home/vdelaluz/git/Distributed-Computing-ENES-UNAM/backup/"


events_list = data['events']

for event in events_list:
    filename = event.get('id') + '.json'
    #my_path = "paolagh@132.247.186.67:public_html/static/backup/"
    with open(PATH+filename, 'w') as outfile:
        json.dump(event, outfile)
    #output = subprocess.run(["scp",filename,"paolagh@132.247.186.67:public_html/static/backup"])

#dating_server = my_path + str(datetime.today())[0:10]
#os.mkdir(dating_server)
#new_path = subprocess.call(['mkdir',dating_server])  

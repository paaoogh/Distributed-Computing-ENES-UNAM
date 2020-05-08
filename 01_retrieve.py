#!/usr/bin/env python3

#Important libraries at the top. For future usage libraries will be commented with a (*)
import json
import requests
import sys
import subprocess
#--------*-----
from datetime import datetime 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

api = "" #credential
response_events = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events")
data = response_events.json()

events_list = data['events']

for event in events_list:
    filename = event.get('id') + '.json'
    my_path = "paolagh@132.247.186.67:public_html/static"
    with open(filename, 'w') as outfile:
        json.dump(event, outfile)  
    output = subprocess.run(["scp",filename,"paolagh@132.247.186.67:public_html/static"])
    output = subprocess.run(["mv","~/public_html/static/"+filename,"/home/paolagh/json/backup/"])


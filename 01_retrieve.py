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

print(events_list[1])
for event in events_list:
    filename = event.get('id') + '.json'
    with open(filename, 'w') as outfile:
        json.dump(event, outfile)
    #with open(filename,"w") as file:
     #   file.write(event)
    output = subprocess.run(["scp",filename,"paolagh@132.247.186.67:public_html/static"])
    output = subprocess.run(["mv",filename,"paolagh@132.247.186.67:json/backup"])


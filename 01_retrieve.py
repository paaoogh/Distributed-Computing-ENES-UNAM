#!/usr/bin/env Python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#Fetching data from EONET: credentials needed in first instance   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#Important libraries at the top. For future usage libraries will be commented with a (*)
import json
import requests
#--------*-----
from datetime import datetime 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

api = "" #credential
response_events = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events/geojson?limit=5&days=20&source=InciWeb&status=open")
data = response_events.json()

events_keys = data.keys()
events_vals = data.values()

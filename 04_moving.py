#!/usr/bin/env python3

import shutil
import os
import subprocess
#--------*-----
from datetime import datetime

backup= "/home/paola/Documents/FILES"
git = "/home/paola/Documents/Distributed-Computing-ENES-UNAM/"
server = "paolagh@132.247.186.67/public_html/static/backup"

dating = str(datetime.today())[0:10]
new_folder = backup + '/' + dating
dating_server = server + "/" + dating
try:
    os.mkdir(new_folder)

except OSError:
    print("Creation of the directory %s failed" % dating)
else: 
    print ("Successfully created the directory for %s" % dating)

for file in os.listdir("/home/paola/Documents/"):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        new_path = shutil.move("/home/paola/Documents/"+filename, new_folder)
#!/usr/bin/env python3

#Important libraries at the top. For future usage libraries will be commented with a (*)
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import subprocess
#_______________*_____________________

PATH1 = "/home/paola/Documents/Computo_distribuido/git"
PATH2 = "/home/paolagh/public_html/static/"

with open(PATH1+'/db.json') as json_file:
        config=json.load(json_file)

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  query1 = ("INSERT INTO events(id, title, magnitude, units, type) VALUES(%s, %s, %s, %s, %s)")

  for filename in glob.glob(PATH2+"*.json"):
    print(filename)

    with open(filename,'r') as file:
        data=json.load(file)

    columns_events = data.keys()
    data_geometry = data.get("geometry")
    columns_geometry = data_geometry.keys() #part of the columns will be on another table

    id_pk = data[columns_events[0]]
    title = data[columns_events[1]]
    magnitude = float(data[columns_geometry[0]])
    units = data[columns_geometry[1]]
    geojson_type = data[columns_geometry[4]]

    data_query = (id_pk, title, magnitude, units, geojson_type)
    cursor.execute(query,data_query)
    cnx.commit()
    output = subprocess.run(["mv",filename,PATH+"backup/"])

    #Not necessary but may be scalable to more tables in database
    #description = columns_events[2]         #
    #status = columns_events[4]              #
    #units = columns_geometry[1]             #
    #geojson_type = columns_geometry[3]      #
    #########################################
    
  
    #flux = float(root[1].text)
    #satellite = int(root[2].text)
    #data_query = (mydate, flux, satellite)

    #print(mydate
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
    else:
            print(err)
else:
        cnx.close()

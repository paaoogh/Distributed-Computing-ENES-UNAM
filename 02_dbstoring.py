#!/usr/bin/env python3

#Important libraries at the top. For future usage libraries will be commented with a (*)
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import subprocess
#_______________*_____________________
import numpy as np

PATH1 = "/Users/paogh/Documents/Computo_distribuido/git/"
#PATH2 = "paolagh@132.247.186.67:public_html/static/"
PATH2 = "/Users/paogh/Documents/Computo_distribuido/git/Distributed-Computing-ENES-UNAM/"

with open(PATH1+'db.json') as json_file:
        config=json.load(json_file)

try:
  cnx = mysql.connector.connect(**config,auth_plugin='mysql_native_password')
  cursor = cnx.cursor()
  query1 = ("INSERT INTO events(id, title, description) VALUES(%s, %s, %s)")
  query2 = ("INSERT INTO geometry(id_geom, id_events, magnitude, units, type_geo) VALUES(%s, %s, %f, %s, %s)")

  for filename in glob.glob(PATH2+"*.json"):
      print(filename)

      with open(filename,'r') as file:
          data=json.load(file)


      id_events = data.get("id")
      title = data.get("title")
      description = data.get("description")

      data_query1 = (id_events, title, description)
      cursor.execute(query1,data_query1)
      print("hey")
"""
      increment = 1
      data_geometry = data.get("geometry")
      for geo in data_geometry:
              magnitude = geo.get("magnitudeValue")
              if magnitude == None:
                magnitude = np.nan
              else:
                magnitude = float(magnitude)
              units = geo.get("magnitudeUnit")
              if units == None:
                units = "NONE"
              type_geo = geo.get("type")
              id_geo = str(increment)+ "_" + filename[-15:-5]

              data_query2 = (id_geo, id_events, magnitude, str(units), str(type_geo))
              cursor.execute(query2,data_query2)
              increment += 1
"""
      cnx.commit()
      #output = subprocess.run(["mv",filename,PATH+"backup/"])

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
    else:
            print(err)
else:
    cnx.close()

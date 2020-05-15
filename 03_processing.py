#!/usr/bin/env Python3

#Important libraries at the top. For future usage libraries will be commented with a (*)
import json
from datetime import datetime
#______________*________
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import subprocess
import mysql.connector
from mysql.connector import errorcode


PATH1 = "/Users/paogh/Documents/Computo_distribuido/git/" #Paola's directory

with open(PATH1+'db.json') as json_file:
    config=json.load(json_file)
    
magnitudes_ = [] #x axis
dates_ = [] #y axis
    
try:
    cnx = mysql.connector.connect(**config, auth_plugin="mysql_native_password")
    cursor = cnx.cursor()
    query = ("SELECT magnitude, date FROM geometry WHERE magnitude>= 50 ORDER BY date")
    cursor.execute(query)

    for (magnitude, date) in cursor:
        print(f"{date}\t{magnitude}")
        magnitudes_.append(magnitude)
        dates_.append(date)
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()


fig, ax = plt.subplots()
ax.set(xlabel='Dates', ylabel='Events magnitude',
       title='view2D')
#plt.axis([x_A, x_B,  y_A, y_B])
ax.grid()

ax.plot(dates_, magnitudes_)
fig.savefig("/Users/paogh/Documents/Computo_distribuido/git/last_flux.png") #Also Paola's directory

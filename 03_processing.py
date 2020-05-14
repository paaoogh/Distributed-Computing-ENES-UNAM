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


PATH1 = "/Users/paogh/Documents/Computo_distribuido/git/"
with open(PATH1+'db.json') as json_file:
        config=json.load(json_file)

with open('db.json') as json_file:
    config = json.load(json_file)

    magnitudes_ = [] #x axis
    y = []
    
try:
    my_date= datetime.today().strftime('%Y-%m-%d')
    cnx = mysql.connector.connect(**config, auth_plugin="mysql_native_password")
    cursor = cnx.cursor()
    query = ("SELECT magnitude FROM geometry WHERE type_geo="point" ORDER BY type_geo")
    cursor.execute(query)

    for i in cursor:
        magnitudes_.append(i)
        
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
ax.set(xlabel='magnitudes', ylabel='flux',
       title='view3D')
#plt.axis([x_A, x_B,  y_A, y_B])
ax.grid()

ax.plot(x, y)
#fig.savefig("/home/vdelaluz/public_html/static/last_flux.png")

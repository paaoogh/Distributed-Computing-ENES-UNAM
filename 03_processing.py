#!/usr/bin/env Python3

#Important libraries at the top. For future usage libraries will be commented with a (*)
import json
from datetime import datetime
#______________*________
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import subprocess
import mysql.connector
from mysql.connector import errorcode


PATH1 = "/home/vdelaluz/git/Distributed-Computing-ENES-UNAM/" #Paola's directory

with open(PATH1+'db.json') as json_file:
    config=json.load(json_file)
    
magnitudes_ = [] #x axis
dates_ = [] #y axis
aux_dates = []
aux_magnitudes = []
    
try:
    cnx = mysql.connector.connect(**config, auth_plugin="mysql_native_password")
    cursor = cnx.cursor()
    query = ("SELECT magnitude, date FROM geometry WHERE magnitude>= 50 ORDER BY date")
    cursor.execute(query)

    for (magnitude, date) in cursor:
        print(f"{date}\t{magnitude}")
        if not aux_dates or date == aux_dates[-1]:
            aux_magnitudes.append(magnitude)
            aux_dates.append(date)
        else:
            magnitudes_.append(aux_magnitudes)
            dates_.append(aux_dates)
            aux_dates = []
            aux_magnitudes = []
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

dating = str(datetime.today())[0:10] + '.png'

#______________________PLOTTING_____________________________
width = 1.2
dic = {}
keys = []
max_len = len(max(magnitudes_, key=len))
for day in dates_:
    keys.append(day[0])
for i in range(len(keys)):
    dic[keys[i]] = magnitudes_[i]
for i in magnitudes_: #fixing number or measurements
    if len(i) != max_len:
        i.extend([0]*(max_len-len(i)))


fig, ax = plt.subplots(figsize=(17,8))
plt.xlabel("Events per dates")
plt.ylabel("Magnitude per event")
plt.title("Events' Magnitude Measurements for Today")
for i in range(max_len):
    plt.bar(keys, [pt[i] for pt in magnitudes_], width=len(magnitudes_)/8.0, edgecolor='black')

plt.savefig("/home/vdelaluz/public_html/gicc/static/cursos/2020-II/eonet/"+ dating) #Also Paola's directory


'''''
plt.style.use('seaborn-dark')
fig, ax = plt.subplots(figsize=(17, 8))
ax.set(xlabel='Event dating', ylabel='Event magnitude',
       title='Magnitues events for today')
#plt.axis([x_A, x_B,  y_A, y_B])
ax.grid()

ax.bar(dates_, magnitudes_, width=5, align='center')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=35, horizontalalignment='right')
fig.savefig("/home/paola/Documents/"+ dating) #Also Paola's directory
'''''


#subprocess.run(["scp",PATH1 + dating,"paolagh@132.247.186.67:public_html/static/"])

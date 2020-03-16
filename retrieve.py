# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#Fetching data from Twitter: credentials needed in first instance #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import tweepy
import json
import pandas as pd
import csv

#These are the credentials
consumer_key = ''
consumer_token = ''
access_key= ''
access_token =''

#pass twitter credentials to tweepy
authen = tweepy.OAuthHandler(consumer_key, consumer_token) 
authen.set_access_token(access_key, access_token)
api = tweepy.API(authen)

trends = api.trends_place(1)


import json
import requests
import sys
import datetime
import time

import pandas
import tweepy
from TwitterAPI import TwitterAPI
from tweepy import Stream
from tweepy import OAuthHandler
sys.stdout.flush()

# Consumner_key & Secret / Access_Token & Secret
consumer_key = "mq7ecRYTpx3OXcF6E5pCTGZTF"
consumer_secret = "tRboVBFKrnxAXEjaNwwBRfWgZAqXowETSqKOtdSU4RNZUM9NSG"

access_token = "991892597391081473-sXwXOYP253t85KWEBrqs3WPpOu7its4"
access_token_secret = "pPiDRxsb5CZjdyZXZahzlFBl1xwfQ7hTTVxLJdKbA4xwd"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


res_list = ["Nando’s","McDonald’s", "Chipotle","Jack in the box", "KFC", "Subway", "Burger King", "Pizza Hut", "Domino’s",
 "Carl’s JR.", "Green Burrito", "Dunkin’ Donuts", "Tacobell", "Auntie Anne’s", "Cinnabon", "Charleys Philly Steak", "Quiznos",
 "Nathan’s Famous","Red Robin Gourmet Burgers and Brew", "Shake shack", "Five Guys","In-N-Out"]


count = 1
for i in res_list:
    if count == 2:
        break
    print('--------------------------------------------')
    print('res_name : ', i)
    print(api.search_users(i,count=2))
    print('--------------------------------------------')
    count += 1

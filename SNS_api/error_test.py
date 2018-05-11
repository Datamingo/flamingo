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

def instagram_api(keyword):
    url1 = 'https://www.instagram.com/web/search/topsearch/?query='
    url2 = keyword
    url = url1 + url2

    response = requests.get(url)
    response_data = response.json()

    # GET FOLLOWER COUNT & HASHTAG COUNT
    follower_count = response_data['users'][0]['user']['follower_count']
    hashtag_count = 0
    for hashtag in response_data['hashtags']:
        hashtag_count += hashtag['hashtag']['media_count']

    return(follower_count, hashtag_count)

def youtube_id_mapping(input_list):
    out_list = []
    for i in input_list:
        q = i
        key = "AIzaSyCXfJz6Z8X30I9GgFg14z2M6sQfhNObo5U"
        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + q + "&type=channel" + "&key=" + key
        response = requests.get(url)
        response_data = response.json()
        out_list.append(response_data['items'][0]['id']['channelId'])

    return out_list

print(youtube_id_mapping(['burger king','burgerking', 'Burger King']))

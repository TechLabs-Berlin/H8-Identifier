from googleapiclient.discovery import build
from h8-identifier.myAPI import APIKey
import pandas as pd
import json
from .Anwendung import predict
import requests

service = build('youtube', 'v3', developerKey=APIKey)
# get vid id from URL-string

def get_id_from_url(url):
    index = url.find('v=')
    if index != -1:
        id = url[index+2:]
        return id
    else:
        return index
    return id
# MAKES A GET REQUEST AND RETURNS A DICT/JSON

def get_vid_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID,
        maxResults=100
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)
    return json_object

# FILTERS ONLY Comment texts OUT OF DICT AND RETURNS comments as tweet

def filter_for_comments(json):
    # CREATE EMPTY DICT
    count = 0
    tweet = ""
    data = []
    # ITERATE OVER COMMENTS
    for item in json['items']:
        count = count +1
        # GET RELEVANT DATA
        tweet = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
    # FILL IN THE OUTPUT DICT
        data.append({
            'id': count,
            'tweet': tweet
        })
        # IF THERE ARE REPLIES ADD THESE TO THE EXPORT DATA
        if "replies" in item:
            for reply in item["replies"]["comments"]:
                # REPLY COMMENTS HAVE ADDITIONAL KEYS reply_no & parent_comment
                count = count + 1
                tweet = reply["snippet"]["textOriginal"]
                data.append({
                    'id': count,
                    'tweet': tweet
                })     
    return data

# CREATES ENTRY AND EXPORTS IT TO FILE

def create_entry(vidID):
    json = get_vid_data(vidID)
    comments = filter_for_comments(json)
    return comments

def get_prediction(url):
    vidID = get_id_from_url(url)
    return predict(create_entry(vidID))

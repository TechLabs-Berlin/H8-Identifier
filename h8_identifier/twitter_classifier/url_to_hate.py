import os
from googleapiclient.discovery import build
#from ..myAPI import APIkey
import pandas as pd
import json
from .Anwendung import predict
import requests

APIkey = os.environ['APIkey']

service = build('youtube', 'v3', developerKey=APIkey)
# get vid id from URL-string


def get_id_from_url(url):
    index = url.find('v=')
    if index != -1:
        id = url[index+2:]
        return id
    else:
        return index
    return id
# FILTERS ONLY Comment texts OUT OF DICT AND RETURNS comments as tweet


def filter_for_comments(json):
    # CREATE EMPTY DICT
    tweet = ""
    data = []
    # ITERATE OVER COMMENTS
    for item in json['items']:
        # GET RELEVANT DATA
        tweet = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
    # FILL IN THE OUTPUT DICT
        data.append({'tweet': tweet})
        # IF THERE ARE REPLIES ADD THESE TO THE EXPORT DATA
        if "replies" in item:
            for reply in item["replies"]["comments"]:
                # REPLY COMMENTS HAVE ADDITIONAL KEYS reply_no & parent_comment
                tweet = reply["snippet"]["textOriginal"]
                data.append({
                    'tweet': tweet
                })
    return data


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
    data = filter_for_comments(json_object)

    while json_object.get("nextPageToken"):
        request = service.commentThreads().list(
            part="snippet, replies",
            videoId=vidID,
            maxResults=100,
            pageToken=json_object.get("nextPageToken")
        )
        response = request.execute()
        tmp_dict = json.dumps(response, indent=2)
        json_object = json.loads(tmp_dict)
        data.extend(filter_for_comments(json_object))

    # with open('test.json', 'w') as file:
    #     json.dump(data, file)
    return data


def get_prediction(vidID, hate=10):
    prediction = predict(get_vid_data(vidID), hate)
    return prediction

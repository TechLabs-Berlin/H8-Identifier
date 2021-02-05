import os
from googleapiclient.discovery import build
import pandas as pd
import json
from .classifier import predict

APIkey = os.environ['APIkey']


service = build('youtube', 'v3', developerKey=APIkey)

MAX_REQUEST_NUMBER = 20
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
    number_of_requests = 1

    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID,
        maxResults=100
    )
    response = request.execute()
    data = filter_for_comments(response)

    while response.get("nextPageToken") and number_of_requests <= MAX_REQUEST_NUMBER:
        number_of_requests += 1
        request = service.commentThreads().list(
            part="snippet, replies",
            videoId=vidID,
            maxResults=100,
            pageToken=response.get("nextPageToken")
        )
        response = request.execute()
        data.extend(filter_for_comments(response))

    return data

def get_prediction(vidID, hate=10, sensitivity = 0.6):
    prediction = predict(get_vid_data(vidID), hate, sensitivity)
    return prediction
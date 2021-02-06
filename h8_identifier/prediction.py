import os
from googleapiclient.discovery import build
import json
from .twitter_classifier.classifier import predict
from .yt_request import get_id_from_url, service, APIkey

def filter_for_comments(json):
    '''FILTERS ONLY Comment texts OUT OF DICT AND RETURNS comments in dataframe as tweet'''
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

def get_all_vid_data(vidID, MAX_REQUEST_NUMBER = 20):
    '''makes MAX_REQUEST_NUMBER of requests, filters for comments text and returns dataframe'''
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

def get_prediction(vidID, MAX_REQUEST_NUMBER = 20, hate=10, threshold=0.6):
    '''It makes MAX_REQUEST_NUMBER of requests, predict those comments and displays hate comments with highest predictions. Prediction are only maid above a threshold probability.'''
    prediction = predict(get_all_vid_data(vidID, MAX_REQUEST_NUMBER), hate, threshold)
    return prediction

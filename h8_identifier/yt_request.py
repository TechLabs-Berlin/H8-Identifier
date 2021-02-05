from googleapiclient.discovery import build
from .twitter_classifier.url_to_hate import filter_for_comments, service
import json
import requests
import os
import random

APIkey = os.environ['APIkey']


# get vid id from URL-string

def get_id_from_url(url):
    index = url.find('v=')
    if index != -1:
        id = url[index+2:]
        return id
    else:
        return index
    return id


def get_title_and_description(id):
    data = get_vid_data(id)
    title = data["items"][0]["snippet"]["title"]
    description = data["items"][0]["snippet"]["description"]
    chanel_title = data["items"][0]["snippet"]["channelTitle"]

    return title, description, chanel_title


def get_vid_data(vidID):
    data = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?key={APIkey}&part=snippet&id={vidID}')
    data_bytes = data.content
    data_json = data_bytes.decode('utf8')
    json_object = json.loads(data_json)

    return json_object

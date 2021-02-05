from googleapiclient.discovery import build
from .twitter_classifier.url_to_hate import filter_for_comments
import json
import requests
import os

APIkey = os.environ['APIkey']

service = build('youtube', 'v3', developerKey=APIkey)
vidID = "_1M1rhO5rXo"


def get_vid_data(vidID):
    data = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?key={APIkey}&part=snippet&id={vidID}')
    print(data.status_code)
    data_bytes = data.content
    data_json = data_bytes.decode('utf8')
    json_object = json.loads(data_json)

    return json_object


# MAKES A GET REQUEST AND RETURNS A DICT/JSON

def get_comment_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID,
        maxResults=100
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)

    # GENERATES JSON WITH WHOLE DATA FOR A BETTER OVERVIEW

    with open("whole_data.json", "w") as outfile:
        json.dump(json_object, outfile)
    return json_object



def create_entry(vidID):
    json = get_comment_data(vidID)
    comments = filter_for_comments(json)
    return comments

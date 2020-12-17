from googleapiclient.discovery import build
from myAPI import API_Key
import json

service = build('youtube', 'v3', developerKey=API_Key)
vidID = "m0RWSHdS77E"


def get_vid_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)
    return json_object


def filter_for_comments(json):
    comments = []
    for item in json['items']:
        comments.append(item['id'])
    return comments


def create_entry(vidID):
    json = get_vid_data(vidID)
    comments = filter_for_comments(json)
    return comments


print(create_entry(vidID))

with open("sample.json", "w") as outfile:
    json.dump(create_entry(vidID), outfile)

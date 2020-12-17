from googleapiclient.discovery import build
from myAPI import API_Key
import json

service = build('youtube', 'v3', developerKey=API_Key)
vidID = "m0RWSHdS77E"


# MAKES A GET REQUEST AND RETURNS A DICT/JSON

def get_vid_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)

    # GENERATES JSON WITH WHOLE DATA FOR A BETTER OVERVIEW

    with open("whole_data.json", "w") as outfile:
        json.dump(json_object, outfile)
    return json_object

# FILTERS RELEANT DATA OUT OF DICT AND RETURNS ARRAY WITH COMMENTS


def filter_for_comments(json):
    comments = []
    for item in json['items']:
        commentID = item['id']
        comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

        comments.append({
            commentID: {
                'autor': author,
                'comment': comment
            }
        })

    return comments

# CREATES ENTRY AND EXPORTS IT TO FILE


def create_entry(vidID):
    json = get_vid_data(vidID)
    comments = filter_for_comments(json)
    return comments


print(create_entry(vidID))

with open("comments.json", "w") as outfile2:
    json.dump(create_entry(vidID), outfile2)

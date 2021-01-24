from googleapiclient.discovery import build
from myAPI import API_Key
import pandas as pd
import json
from Anwendung import predict

service = build('youtube', 'v3', developerKey=API_Key)
url = https://www.youtube.com/watch?v=6eGEX_LTqhQ 
# https://www.youtube.com/watch?v=suOeUHCadSA 
def get_vidID(url):
    address = str(url)
    vidID = address - "https://www.youtube.com/watch?v="
    return vidID
vidID = "6eGEX_LTqhQ"


# MAKES A GET REQUEST AND RETURNS A DICT/JSON

def get_vid_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)
    return json_object

    # GENERATES JSON WITH WHOLE DATA FOR A BETTER OVERVIEW

    """with open("whole_data.json", "w") as outfile:
        json.dump(json_object, outfile)
    return json_object """


# FILTERS RELEANT DATA OUT OF DICT AND RETURNS NEW DICT

def filter_for_comments(json):
    videoID = json["items"][0]["snippet"]["videoId"]

    # CREATE EMPTY DICT
    count = 0
    tweet = ""
    data1 = []
    data2 = []
    data = {
        "comments_by_ID": {},
        "commentIDs": []
    #  """"authors_by_ID": {},
        # "authorIDs": [] """
    }

    # ITERATE OVER COMMENTS
    for item in json['items']:
        count = count +1

        # GET RELEVANT DATA
        commentID = item['id']
        comment_txt = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        tweet = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
    # """    author_name = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
    #     author_ID = item["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]
    #     timestamp = item["snippet"]["topLevelComment"]["snippet"]["updatedAt"]
    #     top_level = True """

        # FILL IN THE OUTPUT DICT
        data["comments_by_ID"][commentID] = {
            # 'author_ID': author_ID,
            'commetn_txt': comment_txt
        # """    'timestamp': timestamp,
        #     'top_level': top_level,
        #     'videoID': videoID """
        }

        data["commentIDs"].append(commentID)
        data1.append({
            'id': count,
            'tweet': tweet
        })
        data2.append(tweet)
# """ 
#         if not "author_ID" in data["authors_by_ID"]:
#             data["authors_by_ID"][author_ID] = {
#                 "autor_name": author_name,
#                 'author_ID': author_ID
#             }
#             data["authorIDs"].append(author_ID) """

        # IF THERE ARE REPLIES ADD THESE TO THE EXPORT DATA
        if "replies" in item:
            counter = 0
            for reply in item["replies"]["comments"]:

                # REPLY COMMENTS HAVE ADDITIONAL KEYS reply_no & parent_comment
            #   """   parent_comment = commentID
            #     top_level = False
            #     reply_no = counter
            #     counter += 1 """
                commentID = reply["id"]
                comment_txt = reply["snippet"]["textOriginal"]
                count = count + 1
                tweet = reply["snippet"]["textOriginal"]
                # """ author_name = reply["snippet"]["authorDisplayName"]
                # author_ID = reply["snippet"]["authorChannelId"]["value"]
                # timestamp = reply["snippet"]["updatedAt"] """

                data["comments_by_ID"][commentID] = {
                    # 'author_ID': author_ID,
                    'commetn_txt': comment_txt
                #   """   'timestamp': timestamp,
                #     'top_level': top_level,
                #     'videoID': videoID,
                #     'reply_no': reply_no,
                #     'parent_comment': parent_comment """
                }

                data["commentIDs"].append(commentID)
                
                data1.append({
                    'id': count,
                    'tweet': tweet
                })
                data2.append(tweet)

# """ 
#                 if not "author_ID" in data["authors_by_ID"]:
#                     data["authors_by_ID"][author_ID] = {
#                         "autor_name": author_name,
#                         'author_ID': author_ID
#                     }
#                     data["authorIDs"].append(author_ID) """
        #data12 = {"id": data1, "tweet": data2}
        #df = pandas.DataFrame(data={"col1": list_1, "col2": list_2})
    return data1


# CREATES ENTRY AND EXPORTS IT TO FILE

def create_entry(vidID):
    json = get_vid_data(vidID)
    comments = filter_for_comments(json)
    return comments


print(predict(create_entry(vidID)))


#with open("comments.json", "w") as outfile2:
#    json.dump(create_entry(vidID), outfile2)
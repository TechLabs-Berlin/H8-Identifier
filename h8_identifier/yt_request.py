from googleapiclient.discovery import build
import json
import requests
import os

APIkey = os.environ['APIkey']
service = build('youtube', 'v3', developerKey=APIkey)

def get_id_from_url(url):
    '''get vid id from URL-string'''
    index = url.find('v=')
    if index != -1:
        id = url[index+2:]
        return id
    else:
        return index
    return id

def get_data_for_page(id):
    meta_data, activity_data = get_vid_data(id)
    title, description, chanel_title = get_title_and_description(meta_data)
    views, commentCount, likes, dislikes = get_views_commentCount_likes(
        activity_data)

    return title, description, chanel_title, views, commentCount, likes, dislikes

def get_title_and_description(meta_data):
    data = meta_data
    title = data["items"][0]["snippet"]["title"]
    description = data["items"][0]["snippet"]["description"]
    chanel_title = data["items"][0]["snippet"]["channelTitle"]

    return title, description, chanel_title


def get_vid_data(vidID):
    data = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?key={APIkey}&part=snippet&id={vidID}')
    data_bytes = data.content
    data_json = data_bytes.decode('utf8')
    meta_data = json.loads(data_json)

    act_data = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id={vidID}&key={APIkey}'
    )
    act_data_bytes = act_data.content
    act_data_bytes = act_data_bytes.decode('utf8')
    activity_data = json.loads(act_data_bytes)

    return meta_data, activity_data


def get_views_commentCount_likes(activity_data):

    statistics = activity_data["items"][0]["statistics"]
    views = int(statistics["viewCount"])
    commentCount = int(statistics["commentCount"])
    likes = int(statistics["likeCount"])
    dislikes = int(statistics["dislikeCount"])
    print(type(commentCount))

    return views, commentCount, likes, dislikes

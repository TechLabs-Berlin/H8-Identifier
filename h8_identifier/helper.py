from .yt_request import get_vid_data, create_entry
import random

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

from .request import get_vid_data, create_entry
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


def get_five_random_comments(id):
    comments = create_entry(id)
    print("example", comments["comments_by_ID"])
    rand_comments = []
    amount_of_comments = len(comments["commentIDs"])

    for i in range(5):
        rand_comments.append(
            comments["comments_by_ID"][random.randint(1, amount_of_comments+1)])
        print(i)

    return rand_comments


def get_title_and_description(id):
    data = get_vid_data(id)
    title = data["items"][0]["snippet"]["title"]
    description = data["items"][0]["snippet"]["description"]
    chanel_title = data["items"][0]["snippet"]["channelTitle"]

    return title, description, chanel_title

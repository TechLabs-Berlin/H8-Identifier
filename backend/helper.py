from backend import get_vid_data, create_entry

# get vid id from URL-string


def get_id_from_url(url):
    index = url.find('v=')
    if index != -1:
        id = url[index+2:]
        return id
    else:
        return index
    return id


def get_five_comments_from_video(id):
    comments = create_entry(id)


def get_title_and_description(url):
    id = get_id_from_url(url)
    data = get_vid_data(id)
    print(type(data))
    title = data["items"][0]["snippet"]

    print(title)
    return title


get_title_and_description("https://www.youtube.com/watch?v=solmfNYP9b4")

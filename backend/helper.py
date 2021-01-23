from .backend import create_entry

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




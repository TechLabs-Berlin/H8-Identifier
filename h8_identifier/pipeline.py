from .yt_request import get_data_for_page
from .prediction import get_prediction


def generate_output(id):

    comments, count_hate, count, percentage = get_prediction(id)
    title, description, chanel_title, views, commentCount, likes, dislikes = get_data_for_page(
        id)

    data_dict = {
        "title": title,
        "description": description,
        "chanel_title": chanel_title,
        "number_of_comments": commentCount,
        "percent_hate": percentage,
        "views": views,
        "likes": likes,
        "dislikes": dislikes,
        "comments": comments,
        "number_of_analyzed_comments": count
    }
    return data_dict

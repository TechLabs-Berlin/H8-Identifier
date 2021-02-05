import random
from .helper import get_title_and_description
from .twitter_classifier.url_to_hate import get_prediction


def generate_output(id):

    comments, count_hate, count, percentage = get_prediction(id)

    for comment in comments:
        print("TYPE", type(comment))

    title, description, chanel_title = get_title_and_description(id)

    data_dict = {
        "title": title,
        "description": description,
        "chanel_title": chanel_title,
        "number_of_comments": count,
        "percent_hate": percentage,
        "views": random.randint(1, 100001),
        "shared": random.randint(1, 100001),
        "comments": comments
    }
    return data_dict

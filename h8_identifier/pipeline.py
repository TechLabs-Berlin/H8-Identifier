import random
from .helper import get_title_and_description
from .twitter_classifier.url_to_hate import get_prediction


def generate_output(id):

    title, description, chanel_title = get_title_and_description(id)
    total, comments, percentage = get_prediction(id)
    print(total)

    data_dict = {
        "title": title,
        "description": description,
        "chanel_title": chanel_title,
        "number_of_comments": random.randint(1, 101),
        "percent_hate": random.randint(1, 101),
        "views": random.randint(1, 100001),
        "shared": random.randint(1, 100001),
        "comments": comments
    }
    return data_dict

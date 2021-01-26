import random
from backend import get_title_and_description, get_five_random_comments


def generate_output(id):

    title, description, chanel_title = get_title_and_description(id)
    comments = get_five_random_comments(id)

    dummy_dict = {
        "title": title,
        "description": description,
        "chanel_title": chanel_title,
        "number_of_comments": random.randint(1, 101),
        "percent_hate": random.randint(1, 101),
        "views": random.randint(1, 100001),
        "shared": random.randint(1, 100001),
        "comments": comments
    }
    return dummy_dict


dummy_data = generate_output("ind782465")

print(dummy_data)

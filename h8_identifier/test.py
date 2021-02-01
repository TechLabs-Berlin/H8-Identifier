from twitter_classifier.Anwendung import predict
import json, sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

with open('test.json', "r") as file:
    comments = json.load(file)
    hate_comments,_,_,_ = predict(comments)

    for hate_comment in hate_comments:
        print(hate_comment)
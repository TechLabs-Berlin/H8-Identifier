from twitter_classifier.classifier import predict
import json, sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

with open('test.json', "r") as file:
    comments = json.load(file)
    print(predict(comments))

    
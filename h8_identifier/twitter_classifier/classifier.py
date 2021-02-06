# -*- coding: utf-8 -*-
"""TwitterSentimentAnalysis
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i-afabNMIU51TLEwBOhWCLSTgr_bLIpJ
"""

import sklearn
import numpy as np
import pandas as pd
import re
import preprocessor as p
import pickle
import sys
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

np.set_printoptions(threshold=sys.maxsize)

REPLACE_NO_SPACE = re.compile(
    "(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\|)|(\()|(\))|(\[)|(\])|(\%)|(\$)|(\>)|(\<)|(\{)|(\})")
REPLACE_WITH_SPACE = re.compile("(<br\s/><br\s/?)|(-)|(/)|(:).")

with open('h8_identifier/twitter_classifier/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('h8_identifier/twitter_classifier/model.pkl', 'rb') as f:
    svm = pickle.load(f)

def clean_tweets(df):
    tempArr = []
    for line in df:
        # send to tweet_processor
        tmpL = p.clean(line)
        # remove puctuation
        # convert all tweets to lower cases
        tmpL = REPLACE_NO_SPACE.sub("", tmpL.lower())
        tmpL = REPLACE_WITH_SPACE.sub(" ", tmpL)
        tempArr.append(tmpL)
    return tempArr

def predict(df, hate=10, sensitivity = 0.6):
    '''This function takes a dataset with comments labels as tweet and predicts the hatefulness.
    Optional parameters are hate and sensitivity.
    It returns 5 elements in this order [first_hate, count_hate, count_comments, hate_ratio]
    - first_hate: First hate comments as dict
    - count_hate: Total amount of hate comments= sum(y_pred_svm)
    - count_comments: Total amount of comments and subcomments
    - hate_ratio = count_hate/count_comments '''
    test = pd.DataFrame(df)
    test_tweet = clean_tweets(test["tweet"])

    test["clean_tweet"] = test_tweet

    x_test_vec = vectorizer.transform(test_tweet)
 
    y_pred_svm = svm.predict(x_test_vec)
    test["prediction"] = y_pred_svm

    y_pred_proba = svm.predict_proba(x_test_vec)
    proba = []
    for i in y_pred_proba:
        a = i[0]
        proba.append(a)
    test["proba"] = proba
    test_sort = test.sort_values(by=["proba"], ascending=False)

    hateful_comments = test_sort[(test_sort["prediction"]==1) & (test_sort["proba"]>= sensitivity)]
    
    count_hate = len(hateful_comments)
    count_comments = len(y_pred_svm)
    hate_ratio = count_hate/count_comments
    percentage = round(hate_ratio * 100, 2)
    first_hate = hateful_comments[["tweet", "proba"]][:hate]

    return [first_hate.to_dict('records'), count_hate, count_comments, percentage]
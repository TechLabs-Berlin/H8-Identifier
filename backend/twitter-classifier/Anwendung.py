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

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\|)|(\()|(\))|(\[)|(\])|(\%)|(\$)|(\>)|(\<)|(\{)|(\})")
REPLACE_WITH_SPACE = re.compile("(<br\s/><br\s/?)|(-)|(/)|(:).")

def clean_tweets(df):
  tempArr = []
  for line in df:
    # send to tweet_processor
    tmpL = p.clean(line)
    # remove puctuation
    tmpL = REPLACE_NO_SPACE.sub("", tmpL.lower()) # convert all tweets to lower cases
    tmpL = REPLACE_WITH_SPACE.sub(" ", tmpL)
    tempArr.append(tmpL)
  return tempArr

def predict(test):
  test = pd.DataFrame(test)
  print(type(test))
  print(test)
  bla = test.copy()

  test_tweet = clean_tweets(test["tweet"])

  test["clean_tweet"] = test_tweet


  with open('vectorizer', 'rb') as f:
      vectorizer = pickle.load(f)

  x_test_vec = vectorizer.transform(test_tweet)

  with open('model2.pkl', 'rb') as f:
      svm = pickle.load(f)
  y_pred_svm = svm.predict(x_test_vec)

  hatefull_comments = []

  for i, value in enumerate(y_pred_svm):
    if value == 1:
      hatefull_comments.append(bla.iloc[i])

  return [y_pred_svm, hatefull_comments, sum(y_pred_svm)/len(y_pred_svm)]
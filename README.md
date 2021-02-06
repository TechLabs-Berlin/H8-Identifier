# H8-Identifier
## Our mission
There should be no hateful comments on youtube. We wanted to train a classifier, which can differentiate between hate and non-hate speech. h8 identifier should give a warning if the threshold for too much hate is reached before such a message can be spread to cause more harm. The background of our work can be read in this blog https://docs.google.com/document/d/1NstPggR4KkS7970cDHlb0RMnXUuh7GtmsHXo-4QUdsY/edit.


# Get Started

## Clone the repo to your machine

```console
$ git clone https://github.com/TechLabs-Berlin/H8-Identifier.git
```

## Get a Google API-Key
https://developers.google.com/maps/documentation/javascript/get-api-key

## Setup .env file

find .env_sample

replace "YOUR KEY GOES HERE" with your own key

rename file to ".env"
## install dependencies

enter virtual environment. In the console write
```console
pipenv shell
```

then
```console
pipenv install
``` 

## Start app

if you are not in the pipenv shell already enter
```console
pipenv shell
```

then start the application by executing
```console
flask run
```

# The classifier
# How to test the classifier with a youtube url

- get_prediction(vidID) takes a video ID. You have to replace vidID = get_id_from_url(url) in order to directly input a youtube url
- you can test any youtube url using this code

```python
from url_to_hate import get_prediction, get_id_from_url

print(get_prediction(get_id_from_url("https://www.youtube.com/watch?v=6eGEX_LTqhQ")))
```
More information below

## prediction.py takes a youtube video ID and generates predictions
This project defines the function get_prediction(vidID), which takes a youtube video ID. It makes MAX_REQUEST_NUMBER of requests, predict those comments and displays hate comments with highest predictions. Prediction are only maid above a threshold probability. It does so by applying the predict() function from classifier.py

Input: 
- youtube video ID
- MAX_REQUEST_NUMBER of requests
- hate = integer, how many hate comments it should display, by default it is 10
- threshold = a float between 0 and 1. Prediction are only maid above a threshold probability.

Output:
 
- same as predict() see below. 

Comments:
- the classifier works for English comments. Comments in other languages might be predicted as hate although they are not hateful.

Attention:
- With the free quota of the Youtube API *https://developers.google.com/youtube/v3/docs/commentThreads/list* we have limited the number of requests per video to 20. Thus around 2000 comments are analyzed.
  
## classifier.py takes a dataset as input applies the classifier 
This project defines the function predict(df), which applies the trained classifier (model.pkl and vectorizer.pkl) to a data called test.

Input: 
- numpy array or a list with a column label *tweet* containing all youtube comments as input.

Process:
- the data is then transformed into a pandas dataframe
- the tweet column is cleaned from noise
- the vectorizer.pkl is transforming the data for the model (a Support Vector Classification https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- the model is applied and generates output

Output:

  - list in this order [first_hate, count_hate, count_comments, percentage]
  - count_hate: Total amount of hate comments.
  - count_comments: Total amount of comments and subcomments analyzed.
  - percentage: hate_ratio = count_hate/count_comments 
  - first_hate.to_dict('records'): Dictionary of hate comments sorted by probability of prediction.

If you want to analyze the predictions on your own, please take these variables from predict(df).
- y_pred_svm is a list consisting of 1 for hate and 0 for non-hate
- hateful_comments is a list consisting of all comments (tweet) which are labeled as hate (1)

Further details on the pretrained classifier and the training data set can be found in the README.md located in the respective directory ../twitter-classifier

# Frontend


# Contributors
- Thuy Anh Nguyen
- Urs Schmid
- Robin van de Water (UX Design)

We thank our mentor Felix Linker who kept us motivated and gave us guidance and input whenever needed.

# References
1 Youtube API: https://developers.google.com/youtube/v3/docs/comments/list https://github.com/googleapis/google-api-python-client
2 NLP classifier: https://github.com/importdata/Twitter-Sentiment-Analysis/blob/master/Twitter_Sentiment_Analysis_Support_Vector_Classifier.ipynb



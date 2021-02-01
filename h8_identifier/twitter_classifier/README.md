# UPDATE 30.01.2021

Achievements:

- get_prediction(vidID) takes a video ID. You have to replace vidID = get_id_from_url(url) in order to directly input a youtube url
- you can test any youtube url using test.py which has this line of code
```python
from url_to_hate import get_prediction, get_id_from_url

print(get_prediction(get_id_from_url("https://www.youtube.com/watch?v=6eGEX_LTqhQ")))
```
- get_prediction now fetches all comments instead of just 100
- Because it gives you tons of hate comments, I modified the output (Update of predict(df) from Anwendung.py ) as follows 
  - list in this order [first_hate, count_hate, count_comments, percentage]
  - count_hate: Total amount of hate comments= sum(y_pred_svm)
  - count_comments: Total amount of comments and subcomments
  - percentage: gives hate_ratio = count_hate/count_comments as a percentage, it is a string
  - first_hate: First 10 hate comments

More information below

# url_to_hate.py takes a youtube video ID and generates predictions
This project defines the function get_prediction(vidID, hate=10)

Input: 
- youtube video ID
- hate = integer, how many hate comments it should display, by default it is 10

Output:
 
- list in this order [first_hate, count_hate, count_comments, hate_ratio]
- count_hate: Total amount of hate comments= sum(y_pred_svm)
- count_comments: Total amount of comments and subcomments
- hate_ratio = count_hate/count_comments 
- first_hate: First 10 hate comments
  
Comments:
- the classifier works for English comments. Comments in other languages might be predicted as hate although they are not hateful.
- it is a modification of the request.py and can run independently from it, however request.py is still needed for troubleshooting, see below.
- myAPI.py needs to be in the same folder as this file.

Attention:
- Our Youtube API *https://developers.google.com/youtube/v3/docs/commentThreads/list* only has a maximum of 100 Results
- Bug fixed on 30.1.2021: implemented paging, now all comments are fetched from the youtube url
# Anwendung.py takes a dataset as input applies the classifier 
This project defines the function predict(df), which applies the trained classifier (model.pkl and vectorizer.pkl) to a data called test.

Input: 
- numpy array or a list with a column label *tweet* containing all youtube comments as input.

Process:
- the data is then transformed into a pandas dataframe
- the tweet column is cleaned from noise
- the vectorizer.pkl is transforming the data for the model (a Support Vector Classification https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- the model is applied and generates output
- get_prediction now fetches all comments instead of just 100
- Because it gives you tons of hate comments, I modified the output (Update of predict(df) from Anwendung.py )

Output:

  - list in this order [first_hate, count_hate, count_comments, hate_ratio]
  - count_hate: Total amount of hate comments= sum(y_pred_svm)
  - count_comments: Total amount of comments and subcomments
  - hate_ratio = count_hate/count_comments 
  - first_hate: First 10 hate comments

If you want to analyze the predictions on your own, please take these variables from predict(df).
- y_pred_svm is a list consisting of 1 for hate and 0 for non-hate
- hateful_comments is a list consisting of all comments (tweet) which are labeled as hate (1)

# Twitter classifier model twitter_classifier.py

This project classifies tweets, via supervised learning. We load the tweets from the train_data directory.

To run this project install the dependencies, perferably with pipenv
```python
pipenv install
```
Then you can run it with
```python
pipenv run python twittersentimentanalysis.py
```

Right now it generates a trained model.pkl (on train data) and a vectorizer.pkl. Furthermore it tests itself for accuracy and prints the results. 
You can load the model and the vectorizer with the pyhton stdlib *pickle* module:
```python
with open('model.pkl', 'rb') as f:
    svm = pickle.load(f)
```

## Description of the dataset

The objective of this task is to detect hate speech in tweets. For the sake of simplicity, we say a tweet contains hate speech if it has a racist or sexist sentiment associated with it. So, the task is to classify racist or sexist tweets from other tweets.

Formally, given a training sample of tweets and labels, where label '1' denotes the tweet is racist/sexist and label '0' denotes the tweet is not racist/sexist, your objective is to predict the labels on the test dataset.

## Possible criticism with the dataset

1. Train.csv
   
   A few tweets appear to be not correctly labeled, for example the following tweet doesn't include hate:

   `18,1,retweet if you agree!`
2. Test.csv
   
   From our testing tweets labeled as hate by the model don't appear to include hate, for example the following tweet is labeled as hate but is not:

   `49159,"my   song ""so glad"" free download!  #shoegaze #newmusic #newsong"`
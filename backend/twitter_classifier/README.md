# url_to_hate.py
This project defines the function get_prediction(url)
Input: 
- youtube url
Output: 
- y_pred_svm is a list consisting of 1 for hate and 0 for non-hate
- hateful_comments is a list consisting of all comments (tweet) which are labeled as hate (1)
- sum(y_pred_svm)/len(y_pred_svm) is the ratio of hateful comments within all checked comments.
Comments:
- the classifier works for English comments. Comments in other languages might be predicted as hate although they are not hateful.
- it is a modification of the request.py and can run independently from it, however request.py is still needed for troubleshooting, see below.
- myAPI.py needs to be in the same folder as this file.

Issue:
- only 20 comments are fetched from the url. The bug is most likely in one of the 2 functions: *get_vid_data()* or *filter_for_comments()* 
  - another possibility: maybe the free Youtube API only allows us fetch 20 comments? thus the functions are fine.
```python
# MAKES A GET REQUEST AND RETURNS A DICT/JSON

def get_vid_data(vidID):
    request = service.commentThreads().list(
        part="snippet, replies",
        videoId=vidID
    )
    response = request.execute()
    new_dict = json.dumps(response, indent=2)
    json_object = json.loads(new_dict)
    return json_object

# FILTERS ONLY Comment texts OUT OF DICT AND RETURNS comments as tweet

def filter_for_comments(json):
    # CREATE EMPTY DICT
    count = 0
    tweet = ""
    data = []
    # ITERATE OVER COMMENTS
    for item in json['items']:
        count = count +1
        # GET RELEVANT DATA
        tweet = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
    # FILL IN THE OUTPUT DICT
        data.append({
            'id': count,
            'tweet': tweet
        })
        # IF THERE ARE REPLIES ADD THESE TO THE EXPORT DATA
        if "replies" in item:
            for reply in item["replies"]["comments"]:
                # REPLY COMMENTS HAVE ADDITIONAL KEYS reply_no & parent_comment
                count = count + 1
                tweet = reply["snippet"]["textOriginal"]
                data.append({
                    'id': count,
                    'tweet': tweet
                })     
    return data
```

# Anwendung.py takes a dataset as input applies the classifier 
This project defines the function predict(test), which applies the trained classifier (model.pkl and vectorizer.pkl) to a data called test.
Input: 
- numpy array or a list with a column label *tweet* containing all youtube comments as input.
Process:
- the data is then transformed into a pandas dataframe
- the tweet column is cleaned from noise
- the vectorizer.pkl is transforming the data for the model (a Support Vector Classificationhttps://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- the model is applied and generates output
  
Output: 
- y_pred_svm is a list consisting of 1 for hate and 0 for non-hate
- hateful_comments is a list consisting of all comments (tweet) which are labeled as hate (1)
- sum(y_pred_svm)/len(y_pred_svm) is the ratio of hateful comments within all checked comments.

It converts the data to 
# Twitter classifier model (twitter_classifier.py)

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
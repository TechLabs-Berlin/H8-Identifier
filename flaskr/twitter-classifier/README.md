# Twitter classifier

This project classifies tweets, via supervised learning. We load the tweets from the train_data directory.

To run this project install the dependencies, perferably with pipenv
```python
pipenv install
```
Then you can run it with
```python
pipenv run python twittersentimentanalysis.py
```

Right now it just tests itself for accuracy but we pickle the model for future use.
You can load the model with the pyhton stdlib *pickle* module:
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
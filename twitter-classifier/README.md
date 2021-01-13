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

Right now it just tests itself for accuracy but our goal is to pickle the model for future use and apply it to youtube comments.
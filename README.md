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

## Start app

start the application by executing
```console
flask run
```




# Backend
## The classifier
This project defines the function *get_prediction(vidID, hate=10)* which can be run on the server. Here more details: get_prediction(vidID) takes a video ID. You have to replace vidID = get_id_from_url(url) in order to directly input a youtube url
- you can test any youtube url using test.py which has this line of code
```python
from url_to_hate import get_prediction, get_id_from_url

print(get_prediction(get_id_from_url("your-youtube-url")))
```
# url_to_hate.py takes a youtube videoID and generates predictions
This project defines the function get_prediction(vidID, hate=10)

Input: 
- youtube video ID
- hate = integer, how many hate comments it should display, by default it is 10

Output:
 
- list in this order [first_hate, count_hate, count_comments, percentage]
- count_hate: Total amount of hate comments= sum(y_pred_svm)
- count_comments: Total amount of comments and subcomments
- percentage: gives hate_ratio = count_hate/count_comments as a percentage, it is a string
- first_hate: First hate comments
  
Comments:
- the classifier works for English comments. Comments in other languages might be predicted as hate although they are not hateful.
- it is a modification of the request.py and can run independently from it, however request.py is still needed for troubleshooting, see below.
- myAPI.py needs to be in the same folder as this file.

Attention:
- - get_prediction now fetches all comments instead of just 100
- Because it outputs tons of hate comments, the default amount of hate comments displayed is 10

Output: list [first_hate, count_hate, count_comments, hate_ratio]
  - count_hate: Total amount of hate comments= sum(y_pred_svm)
  - count_comments: Total amount of comments and subcomments
  - hate_ratio = count_hate/count_comments 
  - first_hate: First 10 hate comments

Further details on the script, the classifier and the training data set can be found in the README.md located in the respective directory ./twitter-classifier

# Frontend


# Contributors
- Urs Schmidt
- Thuy Anh Nguyen
- Maiuran	
- Robin van de Water

We thank our mentor Felix Linker who kept us motivated and gave us guidance and input whenever needed. 
Thank you Wahid for your input.

# References
1 Youtube API: https://developers.google.com/youtube/v3/docs/comments/list https://github.com/googleapis/google-api-python-client
2 NLP classifier: https://github.com/importdata/Twitter-Sentiment-Analysis/blob/master/Twitter_Sentiment_Analysis_Support_Vector_Classifier.ipynb



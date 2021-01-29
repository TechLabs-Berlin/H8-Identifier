# H8-Identifier
## Our mission
There should be no hateful comments on youtube. We wanted to train a classifier, which can differentiate between hate and non-hate speech. h8 identifier should give a warning if the threshold for too much hate is reached before such a message can be spread to cause more harm. The background of our work can be read in this blog https://docs.google.com/document/d/1NstPggR4KkS7970cDHlb0RMnXUuh7GtmsHXo-4QUdsY/edit.

# Backend
## The classifier
url_to_hate.py takes a youtube url and generates predictions. This project defines the function *get_prediction(url)* which can be run on the server. Here more details: 

Input: 
- a youtube url

Output: 
- y_pred_svm is a list consisting of 1 for hate and 0 for non-hate
- hateful_comments is a list consisting of all comments (tweet) which are labeled as hate (1)
- sum(y_pred_svm)/len(y_pred_svm) is the ratio of hateful comments within all checked comments.

Comments:
- the classifier works for English comments. Comments in other languages might be predicted as hate although they are not hateful.
- it is a modification of the request.py and can run independently from it, however request.py is still needed for troubleshooting, see below.
- myAPI.py needs to be in the same folder as this file.

Attention:
- only 100 comments are fetched from the youtube url due to a limitation of the Youtube API *https://developers.google.com/youtube/v3/docs/commentThreads/list*

Further details on the script, the classifier and the training data set can be found in the README.md located in the respective directory backend/twitter-classifier

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



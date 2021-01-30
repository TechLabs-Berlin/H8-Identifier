# H8-Identifier
## Our mission
There should be no hateful comments on youtube. We wanted to train a classifier, which can differentiate between hate and non-hate speech. h8 identifier should give a warning if the threshold for too much hate is reached before such a message can be spread to cause more harm. The background of our work can be read in this blog https://docs.google.com/document/d/1NstPggR4KkS7970cDHlb0RMnXUuh7GtmsHXo-4QUdsY/edit.

# Backend
## The classifier
This project defines the function *get_prediction(vidID)* which can be run on the server. Here more details: get_prediction(vidID) takes a video ID. You have to replace vidID = get_id_from_url(url) in order to directly input a youtube url
- you can test any youtube url using test.py which has this line of code
```python
from url_to_hate import get_prediction, get_id_from_url

print(get_prediction(get_id_from_url("your-youtube-url")))
```
- get_prediction now fetches all comments instead of just 100
- Because it outputs tons of hate comments, I modified the output (Refer predict(df) from Anwendung.py)

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



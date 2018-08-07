'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Continue your program below!

# Textblob sample:
sentiments = []
for tweet in tweetData:
    tb = TextBlob(tweet['text'])
    sentiments.append(tb.sentiment)

averagePolarity = 0
averageSubjectivity = 0
for item in sentiments:
    averagePolarity += item.polarity
    averageSubjectivity += item.subjectivity
averagePolarity /= len(sentiments)
averageSubjectivity /= len(sentiments)

print("Average polarity: %s" %averagePolarity)
print("Average subjectivity: %s" %averageSubjectivity)

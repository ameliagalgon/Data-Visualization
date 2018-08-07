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
polarity = []
subjectivity = []
for tweet in tweetData:
    tb = TextBlob(tweet['text'])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

hist = plt.hist(polarity, [-1, -0.5, 0, 0.5, 1])
#hist2 = plt.hist(subjectivity, [0, 0.25, 0.5, 0.75, 1])
plt.show()

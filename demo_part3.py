'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Continue your program below!

#combine all the tweets into one large string
allTweets = ""
for tweet in tweetData:
    allTweets += tweet['text']
    allTweets += " "

tb = TextBlob(allTweets)

wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", "automation"]
filteredDictionary = dict()
frequencies = []

for word in tb.words:
	#skip tiny words
    if len(word) < 2:
        continue
	#skip words with random characters or numbers
    if not word.isalpha():
        continue
	#skip words in our filter
    if word.lower() in wordsToFilter:
        continue
	#don't want lower case words smaller than 5 letters
    if len(word) < 5 and word.upper() != word:
        continue

	#Try lower case only, try with upper case!
    freqTuple = (word.lower(), tb.word_counts[word.lower()])
    if freqTuple in frequencies:
        continue
    frequencies.append(freqTuple)
    #filteredDictionary[word.lower()] = tb.word_counts[word.lower()]
print(frequencies)
#Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(frequencies)
#wordcloud = WordCloud().generate(allTweets)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

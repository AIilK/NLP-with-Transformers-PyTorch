tweet = "im alireza and learn how to use huggingface and nlp for transformer and its very good"
from nltk.corpus import stopwords 

stop_words = stopwords.words('english')
tweet = tweet.lower().split()
tweet_no_stopwords = [word for word in tweet if word not in stop_words]
print(' '.join(tweet))
print (' '.join(tweet_no_stopwords))
word = ["happy" , "amazing" , "fully" , "maximum" , "amazed" , "amazing"]

from nltk.stem import PorterStemmer , LancasterStemmer , WordNetLemmatizer , wordnet
porter = PorterStemmer()
lancaster = LancasterStemmer()

stem = [porter.stem(w) for w in word]
stem2 = [lancaster.stem(w) for w in word]
print(stem)
print(stem2)
lemmatizer = WordNetLemmatizer()
lemma = [lemmatizer.lemmatize(word) for word in word]
print(lemma)

lem = [lemmatizer.lemmatize(word , wordnet.VERB) for word in word ] # it can to understand stemm of words 
print(lem)
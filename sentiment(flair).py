import flair 

model = flair.models.TextClassifier.load('en-sentiment')
text = 'i like you'
sentence = flair.data.sentence(text)
sentence.to_tokenized_string()
model.predict(sentence)
print(sentence)

texts = 'i hate you'
sentences = flair.data.sentence(texts)
sentences.to_tokenized_string()
model.predict(sentences)
print(sentences)

print(sentence.get_labels()[0].score)
print(sentence.get_labels()[0].value)
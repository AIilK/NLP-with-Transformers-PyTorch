from transformers import BertForSequenceClassification, BertTokenizer
import torch.nn.functional as f
import torch
modelname = 'ProsusAI/finbert'
model = BertForSequenceClassification.from_pretrained(modelname)
tokenizer = BertTokenizer.from_pretrained(modelname)
txt = "The stock price of Apple Inc. has been rising steadily over the past few months, indicating strong investor confidence in the company's performance and future prospects."
tokenz = tokenizer.encode_plus(txt , max_length = 512 , 
truncation = True, # if more than 512 tokens, it will be truncated (removed)
padding = 'max_leagth' ,# if less than 512 tokens, it will be padded with zeros untill 512 tokens
add_special_tokens = True , # add [CLS] and [SEP] tokens
return_tensors = 'pt') # return pytorch tensors

output = model (**tokenz)
print(output)

probs = f.softmax(output[0] , dim = -1)
prediction = torch.argmax(probs)
print(prediction)
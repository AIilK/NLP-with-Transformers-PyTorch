from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate() #with kaggle file authenticate you have permission 
api.competition_download_file('sentiment-analysis-on-movie-reviews',
                              'test.tsv.zip' , path='./')
api.competition_download_file('sentiment-analysis-on-movie-reviews',
                              'train.tsv.zip' , path='./')

import zipfile
with zipfile.ZipFile ('./test.tsv.zip' , 'r') as zipref:
    zipref.extractall('./')
with zipfile.ZipFile ('./train.tsv.zip' , 'r') as zipref:
    zipref.extractall('./')

import pandas as pd
df = pd.read_csv('train.tsv' , sep= '\t')  
   
from transformers import BertTokenizer 

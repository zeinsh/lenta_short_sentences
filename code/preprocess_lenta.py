import pickle
import re 
from lib.nlp_utils import tokenize_sent
from lib.general_utils import printProgressBar
from lib.textprocessingmd import replaceURL, replaceDigits

from string import punctuation
punctuation+='«»'

def separatePunc(text):
    for c in punctuation:
        text=text.replace(c,' {} '.format(c))
    return text

def processText(text):
    text=text.lower()
    text=replaceURL(text)
    text=separatePunc(text)
    text=replaceDigits(text)
    return text

def splitText(text):
    sentences=[processText(sent) for sent in tokenize_sent(str(text),lang='ru')]
    return [sentence for sentence in sentences if len(sentence.split())<40 and len(sentence)>0]

import pandas as pd
import numpy as np
data=pd.read_csv('lenta/lenta-ru-news.csv')

dictionary={}
corpus=""

count_sentences=0
for i in range(len(data)):
    if i%1000==0:
        printProgressBar(i,len(data),suffix="Extracted sentences {}".format(count_sentences))
    sentences=splitText(data.text.iloc[i])
    corpus+='\n'.join(sentences)+'\n'
    count_sentences+=len(sentences)
print()
with open('output/lenta_corpus_preprocessed.txt','w') as f:
    f.write(corpus)

import pickle
from lib.general_utils import printProgressBar
from lib.filesmd import loadPickle, savePickle

def replaceUNK(text,keep_tokens):
    def mapToken(token,keep_tokens):
        if token in keep_tokens:
            return token
        else:
            return '<unk>'
    return ' '.join(mapToken(token,keep_tokens) for token in text.split())
def checkConditions(text):
    def checkregularization(text,op,cl):
        n1=text.count(op)
        n2=text.count(cl)
        if n1!=n2:
            return False

        n1=0
        for c in text:
            if c==op:
                n1+=1
            elif c==cl:
                n1-=1
            if n1<0:
                return False
        return True
    # check short strings
    if len(text.split())<4:
        return False
    # no english
    enletters='abcdefghijklmnopqrstuvwxyzABCEGHIJKLMOPQRSTUVWXYZ'
    for c in enletters:
        if c in text:
            return False
    # check open close
    opcllist=['«»','()','[]','{}']
    for opcl in opcllist:
        if not checkregularization(text,opcl[0],opcl[1]):
            return False
        
    # check even qutations
    n1=text.count("'")
    if n1%2!=0:
        return False
    n1=text.count('"')
    if n1%2!=0:
        return False
    return True

from collections import Counter

train_size=200000
val_size=16000
test_size=16000
total=train_size+val_size+test_size

dictionary_size=14995
dictionary=loadPickle('output/dictionary.pickle')
keep_tokens=[k for k,v in dictionary.most_common(dictionary_size)]

dataset=[]
with open('output/lenta_corpus_preprocessed.txt','r') as f:
    for line in f:
        if len(dataset)==total:
            break
        if not checkConditions(line.strip()):
            continue
        #print("{} out of {}".format(len(dataset),total))
        if len(dataset)%20==0:
            printProgressBar(len(dataset),total)
        proc_line=replaceUNK(line,keep_tokens)
        
        n_unk=proc_line.count('<unk>')
        n_tokens=len(proc_line.split())
        
        if n_tokens==0: continue
        if n_unk/float(n_tokens)<0.1:
            dataset.append(proc_line)
            
        if len(dataset)%100==0:
            with open('output/examples.txt','a') as fex:
                fex.write(proc_line+'\n')
                
train_text='\n'.join(dataset[:train_size])
valid_text='\n'.join(dataset[train_size:train_size+val_size])
test_text='\n'.join(dataset[-test_size:])

with open('output/lenta.train.txt','w') as f:
    f.write(train_text)
with open('output/lenta.valid.txt','w') as f:
    f.write(valid_text)
with open('output/lenta.test.txt','w') as f:
    f.write(test_text)

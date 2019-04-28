from collections import Counter
from lib.general_utils import printProgressBar
from lib.filesmd import savePickle

dictionary=Counter()

k=0
with open('output/lenta_corpus_preprocessed.txt','r') as f:
    lines=f.readlines()
    total=len(lines)
    for k in range(0,total,10000):
        num_terms=len(dictionary.keys())
        printProgressBar(k,total,suffix="Num terms {}".format(num_terms))
        dictionary+=Counter(' '.join(lines[k:k+10000]).split())
savePickle(dictionary,'output/dictionary.pickle')

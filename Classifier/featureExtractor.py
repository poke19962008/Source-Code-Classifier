'''
Index
    - python: 0
    - c: 1
    - cpp: 2
    - java: 3
'''

from nltk import ngrams
import os, re, pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing

langs = ['py', 'c', 'cpp', 'java']
limit = 90000

def getfiles():
    rootDir = "./data"
    files = [[], [], [], [], []]

    for lang in langs:
        for fname in os.listdir(os.path.join(rootDir, lang)):
            files[langs.index(lang)].append(os.path.join(rootDir, lang, fname))
    return files

def ngram():
    df = pd.DataFrame(columns=['n1', 'n2', 'n3', 'lang'])

    for lang in getfiles():
        limitCounter = 0
        for fs in lang:
            ext = fs.split('/')[-1].split('.')[-1]
            with open(fs, 'r') as f:
                sc = f.read()

                tokens = re.findall(r'[\w\']+|[\"\"!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\"\"\\]', sc)

                for grams in ngrams(tokens, 3):
                    df.loc[len(df)] = [grams[0], grams[1], grams[2], ext]
                    limitCounter += 1

                    if limitCounter >= limit:
                        break
                print "[SUCCESS] Parsed ", fs
                if limitCounter >= limit:
                    break

    with open('parsed.csv', 'w') as f:
        df.to_csv(f)

    print "[SUCCESS] Saved to `parsed.csv`"
    del df

    encode()

def encode():
    print "Started encoding.."
    df = pd.read_csv('parsed.csv')

    X = df[['n1', 'n2', 'n3']].as_matrix().reshape(-1)

    le = preprocessing.LabelEncoder()
    le.fit(X)

    with open('bin/labelEncoder.bin', 'wb') as f:
        pickle.dump(le, f)

    X = le.transform(X).reshape(-1, 3)
    df_ = pd.DataFrame({'n1': X[:,0], 'n2': X[:, 1], 'n3': X[:,2]})
    df.n1, df.n2, df.n3 =  df_.n1, df_.n2, df_.n3
    del df['Unnamed: 0']

    df.to_csv('parsed.csv')


if __name__ == '__main__':
    # encode()
    ngram()

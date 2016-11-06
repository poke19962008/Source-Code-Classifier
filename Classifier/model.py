from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import linear_model
from sklearn import preprocessing
import pandas as pd
import numpy as np
import pickle, re
from nltk import ngrams

langs = ['py', 'c', 'cpp', 'java']

def fit():
    df = pd.read_csv('parsed.csv')

    X = df[['n1', 'n2', 'n3']]
    Y = df.lang

    print "[SUCCESS] Read file `parsed.csv`"
    clf = linear_model.LogisticRegression(verbose=2)
    clf.fit(X, Y)

    print "[SUCCESS] Fitted classifier"
    with open('bin/lr.bin', 'wb') as f:
        pickle.dump(clf, f)
        print "[SUCCESS] Saved classifier"

def preprocess(sc):
    tokens = re.findall(r'[\w\']+|[\"\"!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\"\"\\]', sc)
    X = []

    with open('bin/labelEncoder.bin', 'rb') as f:
        le = pickle.load(f)
        for grams in ngrams(tokens, 3):
            try:
                X.append(le.transform(np.array(grams)))
            except:
                continue
        del le
        print "[SUCCESS] Preprocessed file."
    return np.mat(X)

def predict():
    for lang in langs:
        with open('test/test.%s'%lang, 'r') as f:
            print "Processing test.", lang
            sc = f.read()
            X = preprocess(sc)

            with open('bin/lr.bin', 'rb') as f:
                clf = pickle.load(f)
                uniq, freq = np.unique(clf.predict(X), return_counts=True)
                print np.asarray((uniq, freq)).T
            print "\n\n"

if __name__ == '__main__':
    # getData()
    # saveData()
    # fit()
    predict()

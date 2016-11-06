from markers import pyMarker, cMarker, cppMarkers, javaMarker, rubyMarker
import re, os
import numpy as np

markers = [pyMarker, cMarker, cppMarkers, javaMarker, rubyMarker]
langs = ['py', 'c', 'cpp', 'java', 'ruby']

def predict(sc):
    freqMatch = [0]*len(markers)

    for i in xrange(len(markers)):
        total = 0
        for pat in markers[i]:
            total += len(re.findall(pat, sc))
        freqMatch[i] = total
    freqMatch = np.array(freqMatch, dtype="float16")
    freqMatch = freqMatch/np.sum(freqMatch)
    print dict(zip(langs, freqMatch))

if __name__ == '__main__':
    for test in os.listdir('test'):
        dir_ = os.path.join('test', test)
        print test
        with open('%s'%dir_, 'r') as f:
            predict(f.read())
            print "\n"

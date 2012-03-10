#!/usr/bin/env python
#
__author__ = 'la'
import nltk

#from nltk.book import *
from urllib import urlopen

url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()

tokens = nltk.word_tokenize( raw )

for token in tokens:
    print token
    # fetch the url
    url = "http://conceptnet5.media.mit.edu/data/concept/en/"+token
    json = urlopen(url).read()
    print json
  
    # convert to a native python object
    (true,false,null) = (True,False,None)
    profiles = eval(json)
    





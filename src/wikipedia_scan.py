'''
Created on Mar 9, 2012

@author: Edmon Begoli
'''
import nltk
from urllib import urlopen


url = "http://www.gutenberg.org/cache/epub/1260/pg1260.txt"
raw = urlopen(url).read()

tokens = nltk.word_tokenize( raw )



"http://en.wikipedia.org/wiki/Dislike"

'''
Created on Mar 9, 2012

'''
__author__ = 'Edmon Begoli'
import nltk 
from urllib import urlopen

def lookup_conceptnet( raw ):

    tokens = nltk.word_tokenize(raw)

    for token in tokens:
        print token
        # fetch the url
        url = "http://conceptnet5.media.mit.edu/data/concept/en/" + token
        json = urlopen(url).read()
        print json
  
        # convert to a native python object
        (true, false, null) = (True, False, None)
        profiles = eval(json)
        
def main():
    pass        
        
if __name__ == '__main__':
    main()

    
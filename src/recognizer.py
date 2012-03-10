#!/usr/bin/env python
#
__author__ = 'la'
import nltk

#from nltk.book import *
from urllib import urlopen

url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()

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
    

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names


def extract_entities( raw ):    
    
    sentences = nltk.sent_tokenize(raw)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)    
    return chunked_sentences
    entity_names = []    

    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        
        entity_names.extend(extract_entity_names(tree))
    
    # Print all entity names
    #print entity_names
    
    # Print unique entity names
    print set(entity_names)

def main():
    pass

if __name__ == '__main__':
    main()


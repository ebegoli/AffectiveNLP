#!/usr/bin/env python
#
__author__ = 'Edmon Begoli'
import nltk

#from nltk.book import *
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()


def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names


def extract_chunked_sentences( raw ):
    sentences = nltk.sent_tokenize(raw)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)    
    return chunked_sentences

def extract_entities( chunked_sentences ):    

    entity_names = []    

    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        
        entity_names.extend(extract_entity_names(tree))
    
    # Print all entity names
    #print entity_names
    
    # Print unique entity names
    print set(entity_names)

def extract_pos( raw ):
    text = nltk.word_tokenize( raw )
    return nltk.pos_tag( text )
    

def main():
    raw = "Peter loves New York City."
    print extract_pos( raw )
    print extract_entities( extract_chunked_sentences( raw ) )

if __name__ == '__main__':
    main()


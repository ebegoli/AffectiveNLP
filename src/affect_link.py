
#!/usr/bin/env python
'''
 get the POS and link it with wordnet, wordnet-affect
 and measure afect
'''
__author__ = 'Edmon Begoli'

from urllib import urlopen
from nltk import *
from nltk.corpus import wordnet as wn

link = "http://legacy.c-span.org/newsmakers/schu.htm"

def pos_sentences( raw ):
    """ Segments the raw text into sentences, tokenizes them and 
        and assigns to each a POS tag
    """    
    sentences = nltk.sent_tokenize(raw)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    return tagged_sentences    

def main():
	print "something"
	html = urlopen(link).read()
	raw = nltk.clean_html(html)
	#print nltk.word_tokenize(raw)  
	print "POS" 
	raw = "Edmon goes to UTK. Anastasia dances. Anthony is a crazy guy."
	sentences = pos_sentences( raw )
	for sentence in sentences:
		print "original sentence: " + str(sentences) + "POS chunks: \n"
		for pos in sentence:
			print "-"
			print pos
			#print wn.synsets( pos[0] )

if __name__ == '__main__':
	main()

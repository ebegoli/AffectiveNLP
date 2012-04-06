
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

def main():
	print "something"
	html = urlopen(link).read()
	raw = nltk.clean_html(html)
	#print nltk.word_tokenize(raw)  
	print "POS" 
	words = nltk.word_tokenize(raw)
	for pos in nltk.pos_tag(words):
		print "-"
		print pos
		print wn.synsets( pos[0] )

if __name__ == '__main__':
	main()

#!/usr/bin/env python
'''
 get the POS and link it with wordnet, wordnet-affect
 and measure afect
'''
__author__ = 'Edmon Begoli'

from urllib import urlopen
from nltk import *
from nltk.corpus import wordnet as wn
from StringIO import StringIO
from zipfile import ZipFile
from pymongo import Connection

#mongodb://<user>:<password>@dbh45.mongolab.com:27457/asd-text

conn = Connection('dbh45.mongolab.com',27457 ) 
db = conn['asd-text']
db.authenticate( 'asdadmin','asdadmin' )


link = "http://legacy.c-span.org/newsmakers/schu.htm"

print db.collection_names()

def get_childes():

	url_dir = 'http://childes.psy.cmu.edu/data/Clinical/'
	listing_html = urlopen(url_dir).read()
	zip_files = [ str(url_dir + zip_file) for zip_file in nltk.clean_html( listing_html ).split(' ') if str(zip_file).endswith('.zip')]
	print 'test'

	for zip_file_url in zip_files:
		print 'examining ' + zip_file_url
        zipfile = ZipFile(StringIO(urlopen( zip_file_url ).read()))
        print zipfile.namelist()  

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
	pass

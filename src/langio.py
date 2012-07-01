""" A collection of utilities for I/O of language oriented data structures - 
    graphs, lists, dictionaries, text files and databases
""" 
__author__ = "Edmon Begoli"


from json import dumps, load
import numpy
from pprint import pprint
import sqlite3
from bulbs.graph import Graph
from nltk.corpus import wordnet as wn

def load_json( filename ):
	''' '''
	with open( filename ) as rd:
		return load( rd )


def save_json( filename, content ):
	''' '''
	with open( filename,'w' ) as writer:
		js = dumps( content )
		writer.write( js )	

def populate_graph( graph_name ):
	g = Graph('http://localhost:8182/graphs/affects')
	print g.V
	for key, value in emotions.iteritems():
		emotion = g.vertices.create({'name':key, "pos":value})
        print g.V


def write_wordnet():

    with open('../data/4000_and_wordnet.txt','w') as wn_4000:
	for key, value in emotions.iteritems():
		wn_4000.write( '\n' + key )
		for synsets in wn.synsets(key):
			wn_4000.write( '\n   ' + str(synsets) )

def ngrams_pos_to_sql( source, target, delimiter, nsize ):
	with open( source ) as source_file:
		for line in source_file:
		    parts = line.split( delimiter )
		    print parts

def ngrams_to_rel():
	pass


def emotions_to_rel():
	with sqlite3.connect( '../data/emotions.dat' ) as conn: 

		c = conn.cursor()
		c.execute( 'drop table if exists emotions')
		c.execute('''create table emotions (name text, pos text, description text, related text) ''')

        for e_key, e_val in emotions.items():
            print e_key + ' ' + e_val
            c.execute('insert into emotions(name,pos) values ( \'' + 
            	str(e_key).replace("'","\'") + '\',\'' + 
            	str(e_val) + '\')')

        conn.commit() 
        print "done"

if __name__ == "__main__": 
	ngrams_pos_to_sql( '../data/w5c.txt', 'ngram5pos.dat', '\t', 5 )
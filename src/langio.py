""" A collection of utilities for I/O of language oriented data structures - 
    graphs, lists, dictionaries, text files and databases
""" 
__author__ = "Edmon Begoli"

import json
import numpy
from pprint import pprint
import sqlite3
from bulbs.graph import Graph
from nltk.corpus import wordnet as wn

def load_json( filename ):
	pass


emotions = {}
emotions_matrix = []

with open('4000_emotions.json') as json_data:
	emotions = json.load(json_data)
	print emotions['love']


def populate_graph():
	g = Graph('http://localhost:8182/graphs/affects')
	print g.V
	for key, value in emotions.iteritems():
		emotion = g.vertices.create({'name':key, "pos":value})
        print g.V


def write_wordnet():

    with open('4000_and_wordnet.txt','w') as wn_4000:
	for key, value in emotions.iteritems():
		wn_4000.write( '\n' + key )
		for synsets in wn.synsets(key):
			wn_4000.write( '\n   ' + str(synsets) )

def main():

	with sqlite3.connect( 'emotions.dat' ) as conn: 

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
	write_wordnet()

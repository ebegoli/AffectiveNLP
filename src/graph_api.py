#!/usr/bin/env python
''' Interface to Graph database for storage
and retrieval of graph representation of terms
'''
__author__ = 'Edmon Begoli'
from bulbs.graph import Graph
import emotions

g = Graph('http://localhost:8182/graphs/affects')
#g = Graph()

def main():
    print g.V

    for key, value in emotions.parrot_primary.iteritems():
        print '\t' + key
        for sec, secval in value.iteritems():
            print '\t' + sec
            primary = g.vertices.create({'name':key})
            secondary = g.vertices.create({'name':sec})
            g.edges.create(primary,"primary",secondary)
    print g.E
    
if __name__ == '__main__':
    main()
#!/usr/bin/env python
"""
 Used for loading of textual or other data affect-related resources into 
 local databases
"""
import sqlite3

conn = sqlite3.connect( 'resources.dat')

def test():

	c = conn.cursor()

	# Create table
	c.execute('''create table emotions (name text, description text, related text) ''')

	# Insert a row of data
	c.execute('''insert into emotions values 
		('love','primary emotions','affections')''')

	# Save (commit) the changes
	conn.commit()
	print "done" 

	# We can also close the cursor if we are done with it
	c.close()

def main():
    test() 

if __name__ == "__main__":
	test()

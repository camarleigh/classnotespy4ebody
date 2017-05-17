#Exercises from Section 4/5 - Using Databases with Python 

# SQL PRACTICE - sqlex1.py/sqlex2.sqlite
# Write a program that intakes a file, counts the num of email msgs per org.
# use a db that has the given schema to keep track of the counts.

import sqlite3
import re

conn = sqlite3.connect('sqlex2.sqlite')
cur = conn.cursor()

#print dir(cur)

cur.execute('''DROP TABLE IF EXISTS Counts ''')

cur.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')

fname = raw_input("file name pls:")
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
  if not line.startswith('From: '): continue
  pieces = line.split("@")
  org = pieces[1]
  #org = re.findall('@([^ \.]*)\.', start)
  #print org
  cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
  #? serves as a placeholder. (org,) is a tuple
  try:
    count = cur.fetchone()[0]
    cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (org,))
  except:
    cur.execute('''INSERT INTO Counts(org,count) VALUES(?,1)''', (org, ))
    conn.commit

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
  print str(row[0]), row[1] #row[0]=org, row[1]=count
cur.close()



#CONNECTING XML TO A DB - xml2db.py

# intake an XML file, create new tables, 
# return specific table of joined tables

import xml.etree.ElementTree as ET 
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

#make new tables in SQL 
cur.execute('''
  CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
) ''')

cur.execute(''' 
  CREATE TABLE IF NOT EXISTS Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
)''')

cur.execute('''
  CREATE TABLE IF NOT EXISTS Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)''')

cur.execute(''' 
  CREATE TABLE IF NOT EXISTS Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER
)''')

fname = raw_input("file name pls:")
if (len(fname) < 1) : fname = 'library.xml'

def lookup_tracks(d, key):
  found = False
  for child_record in d:
    if found : return child_record.text 
    if child_record.tag =='key' and child_record.text == key : 
      found = True
  return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict Count:', len(all)
for entry in all:
  if lookup_tracks(entry,'Track ID') is None : continue
  name = lookup_tracks(entry,'Name')
  artist = lookup_tracks(entry, 'Artist')
  album = lookup_tracks(entry, 'Album')
  genre = lookup_tracks(entry, 'Genre')

  if name is None or artist is None or album is None or genre is None : continue
  print name, artist, album, genre

  cur.execute(''' INSERT OR IGNORE INTO Artist(name) VALUES(?)''', (artist, ))
  cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
  artist_id = cur.fetchone()[0]


  cur.execute(''' INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?,?)''',
    (album, artist_id))
  cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
  album_id = cur.fetchone()[0]

  cur.execute(''' INSERT OR IGNORE INTO Genre(name) VALUES(?)''', (genre, ))
  cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
  genre_id = cur.fetchone()[0]

  cur.execute(''' INSERT OR REPLACE INTO Track(title, album_id, genre_id) VALUES(?,?,?)''',
   (name, album_id, genre_id))

  conn.commit()



#CONNECTING JSON TO A DB - json2dbex.py

# read data from a JSON format, parse file, produce SQLite db,
# w/ user, course, and member tables

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print name, title, role

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?,? )''', 
        (user_id, course_id, role) )

    conn.commit()







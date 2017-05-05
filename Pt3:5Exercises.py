#Exercises from Section 3/5 - Using Python to Access Web Data 

#REGEX PRACTICE - regexsum.py
# Read a file: use regex to find lines with numbers in them
# Return sum of said numbers
import re

nfile = raw_input("file name please:")
handle = open(nfile,'r')

#x = "a need 256 to add to 456 and give me a big number 23 in return"
sum = 0
for line in handle:
  #line = line.rstrip()
  #if re.search('[0-9]*', line):
    #print line
  y = re.findall('([0-9]+)', line)
  for vals in y:
    sum = float(vals) + sum
print sum

#SCRAPING PRACTICE(1/2) - firstscrape.py
# open web page, read all span tags, sum their comments
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0
taglist = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    tag = tag.contents[0]
    sum = int(tag) + sum
print sum    
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs


#SCRAPING PRACTICE(2/2) - secscrape.py
# open web page, extract href values, 
# find diff tag in relation to 1st taglist
# follow that link, repeat x times
# report last name found
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = raw_input('Count:')
count = int(count)
position = raw_input('Position:')
position = int(position)
print "Retrieving:", url
i = 0
while i < count: # for the length of count, loop through the following steps
  tags = soup('a') #find all a href tags on this page
  #toi =  tags[position - 1] #find the position value in the list [2]
  new_url = tags[position - 1].get('href', None) #assign url value to position value
  print "Retrieving:", new_url #print the position value in the list
  new_html = urllib.urlopen(new_url).read()
  soup = BeautifulSoup(new_html)  #make soup with new url
  i = i+1 


#XML Exercises - xmlex.py
# take in a URL, parse & extract comment counts from XML,
# compute sum of paragraphs, enter the sum

import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

count = 0
sum = 0
results = tree.findall('.//count')

for result in results:
    result = int(result.text)
    sum = result + sum
    count = count + 1
print 'Count:', count
print 'Sum:', sum


#JSON Exercises - jsonex.py
# take in a URL, parse & extract comment counts from JSON,
# compute sum of paragraphs, enter the sum


import urllib
import json

address = raw_input("Please enter an an address:")
url = urllib.urlopen(address)
print "Retrieving", address
data = url.read()
print "Retreived", len(data), "characters"
js = json.loads(data)
info = json.dumps(js, indent = 4)
temp_list = js["comments"]
#print temp_list
sum = 0
count = 0
for items in temp_list:
  sum = int(items["count"]) + sum
  count = count + 1
print count
print sum


#API PRACTICE - geolook.py
# prompt for location, contact a web service, retrieve JSON
# parse, retrieve first 'place_id' from JSON
#(place_id is a textual identifier that uniquely ids a place as 
#  within googlemaps API)

import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)

    place_id = js["results"][0]["place_id"]
    print "Place id:", place_id

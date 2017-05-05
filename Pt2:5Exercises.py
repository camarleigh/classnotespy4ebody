#Exercises from Section 2/5 - Python Data Structures

#Use find() and string slicing to get desired output. 
#Convert output to float and print.

text = 'X - DSPAM - Confidence:  '

#my answer
start = text.find('.')
target = text[start-1:]
fin = float(target)
print fin 

#their answer
start = text.find(':')
print start
print text[start-1:]
num = float(text[start-1:])
print num

# Write a prog that prompts for file name, opens file, reads file
#prints content of file in uppercase.

file_name = raw_input('file name, please')
file_handle = file_name.open('word.txt', 'r')
for line in file_handle:
  line = line.strip()
  line = line.upper()
  # you could combine the two: 
  #line = line.strip().upper()
  print line

# Write a prog that prompts for file name, opens file, reads file
#look for specifc lines, count those lines and extract the floating
# point value and compute the avg for given  output desired. 
# DO NOT USE SUM OR AVG functions

# First Attempt: ( almost right, but not quite)
fname = raw_input("file name,please: ")
fhandle = open(fname, 'r')
count = 0
for line in fhandle:
  if not line.startswith('X-DSPAM-Confidence:'):
    continue
  line = line.strip()
  pos = line.find(':')
  num = float(line[pos+1:])
  total = total + num
  count = count + 1
  print "Average Spam Confidence: ", total/count

# Second Attempt: (right!)
fname = raw_input("file name,please: ")
fhandle = open(fname, 'r')
count = 0
total = 0
avg = 0
for line in fhandle:
  line = line.strip()
  if line.startswith('X-DSPAM-Confidence:'):
    pos = line.find(":")
    num = float(line[pos+1:])
    total = total + num
    count = count + 1
    avg = float(total/count)
print "Average Spam Confidence:", avg

#SPLIT PRACTICE(1/2)
# Write a prog  that opens a file, reads it. For each line,
# split line into new list of words. For each word, check to see
# if word is already in the list, and if not add it to the list.
# Sort and print resulting list

fname = raw_input("file name pls: ")
fhandle = open(fname,'r')
first = list()
for line in fhandle:
  line = line.rstrip()
  line = line.split()
  for word in line:
    if not word in first:
      first.append(word)
      first.sort()
print first

#SPLIT PRACTICE(2/2)
# Write a program theat opens a file, reads it and for each line that
# starts with 'From:', parse line using split, print  the email address
# and print the count of emails at the end.

fname = raw_input("file name pls: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fhandle = open(fname, 'r')
count = 0
countlist = []
for line in fhandle:
  line = line.rstrip()
  if line.startswith('From:'):
    line = line.split()
    print line[1]
    countlist.append(line[1])
    count = len(countlist)
print "There were ", count, "lines in the file with From as the first word."

#DICTIONARY PRACTICE
# Write a program to read a file and determine who's sent the most emails
# Look for 'From' lines, 2nd word of said line is sender
# Create a py dict that maps sender to count
# After dict created read to get a most count

name = raw_input("file name:")
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name, 'r')
addys = list()
for line in handle:
  line = line.rstrip()
  if line.startswith("From:"):
    line = line.split()
    line = line[1]
    addys.append(line)
dictpract = dict()
for addy in addys:
dictpract[addy] = dictpract.get(addy, 0) + 1
emailsender = None
numemails = None
for email, count in dictpract:
  if count is None or count < numemails:
    numemails = count
    emailsender = email
print emailsender, numemails

#TUPLES PRACTICE
# Write a program that takes in a file and reads it
# tells you what the distribution of msgs by hour of day
# the hour can be found in lines that start with "From:"
# once you have counts, print out with hour, sorted

name = raw_input("file name,pls: ")
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name, 'r')
lst = list()
for line in handle:
  if line.startswith("From:"):
    line = line.split(":")
    line = line[0]
    line = [-2: ]
    lst.append(line)
    if "om" in lst: lst.remove("om")
dct = dict()
for hours in lst:
  dct[hours] = dct.get(hours, 0) + 1
another_lst = list()
for stuff in dct:
  another_lst = dct.items()
  another_lst.sort(reverse = False)
  for hour,num in another_lst:
    print hour,num
#-------------- OR -----------------
another_lst = list()
for hour,num in dct.items():
  another_lst.append(hour,num)
  another_lst.sort(reverse = False)
for hour,num in another_lst:
  print hour, num

 


#Exercises from Section 1/5 - Python for Everybody

#Write a program that prompts for integers until user enters done.
#Once done is entered, print largest & smallest of the numbers. If user
#enters anything other than int or done, catch it w/ try/except, give approp.
#msg & ignore the input

# BREAK IT DOWN: READ THE INPUT, CHECK THE DATA IS GOOD, DO THE WORK

smallest = None
largest = None
while True:
  num = raw_input('enter a number:')
  if num == "done": break
  try:
    num = int(num)
  except: 
    print "invalid input"

  if smallest is None:
    smallest = num
  elif smallest > num:
    smallest = num
  elif smallest < num:
    if largest is None:
        largest  = num
    elif largest < num:
        largest = num

print "Maximum is  ", largest
print "Minimum is  ", smallest

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
  # you could combine the two: line = line.strip().upper()
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


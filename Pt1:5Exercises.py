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


# Code 1: Learning how to print text in python

print "First Assignment: Taking Screenshots"

# Code 2: Learning application of conditional statements in Python

x = 5
if x == 5: print "equal's 5"
if x >= 5: print "more than or equal to 5"
if x < 5: print "less than 5"
if x != 6: print "la la la la"

# Code 3: Learning application of if else structure and while loop
x = 0

while x<100:
	if x < 2: print "small"
	elif x < 10: print "medium"
	elif x < 20: print "big"
	elif x < 40: print "large"
	elif x < 100: print "huge"
	else: print "ginormous"
	x=x+1
	
# Code 4: Learning how to accept user input and do error handling using try, except statement
rate =raw_input("enter the rate?")
hrs= 40
try:
	# if the below statement throws and error then python will execute statements 
	# under except if it doesn't throw an error python will ignore statements under except
	rate=int(rate) 
except:
	rate=0

pay=rate*hrs

print "the pay of the employee is",pay

# Code 5: learning simple computation using python

hrs = raw_input("enter the hours: ")
hrs = float(hrs)

rate = raw_input("enter the rate: ")
rate = float(rate)

if hrs <= 40 :
	pay=rate*hrs
	print ("the pay is"),pay
else:
	pay=rate*40+(hrs-40)*(1.5*rate)

print pay


# Code 6: One more example of if else structure
score = raw_input("Enter Score: ")

try:
	score=float(score)
	if 0 <= score <= 1:
		if score >= 0.9:
			print "A"
		elif score >= 0.8:
			print "B"
		elif score >= 0.7:
			print "C"
		elif score >= 0.6:
			print "D"
		else: 
			print "F"
	else:
		print "Enter the score between 0 and 1"
		
except:
	print "Enter a numeric input"
	
# Code 6: Learning to define functions in python

x=5

print "hello"

def func1():
	print "this is my first function"
	print "I nailed it"
	
func1()

print "yes",x









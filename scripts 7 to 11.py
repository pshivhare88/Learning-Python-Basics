

# Code 7: Learning to define a function with an argument.

def greet(lang): 
    if lang=="es":
        print "Hola"
    elif lang=="fr":
        print "Bonjour"
    else:
        print "Hello"

greet("en")
greet("fr")
greet("es")


# Code 8: One more example on function

def computepay(h,r):
    if h <= 40:
        pay=h*r
    else:
        pay=r*40+(h-40)*1.5*r
    return pay

hrs = raw_input("Enter Hours:")
hrs=float(hrs)
rate=raw_input("Enter Rate:)
rate=float(rate)

p= computepay(hrs,rate)
print p


# Code 9: learning applying while loop

l= None
s= None

while True:
    num=raw_input("Enter a Number:") #python keeps asking users for number until user inputs string "done"
    if num == "done":
        break
    else:
        try:
            num=float(num)
            if l is None: 
                l=num
            elif num > l:
                l=num
            
            if s is None:
                s=num
            elif num < s:
                s=num
        except:
            print ("Invalid input")

print ("Maximum is"),l
print ("Minimum is"),s

# Code 10: generating a boolean variable

x=33
y= x== 100
print y

#Output
#False


# Code 11: Subsetting a string by extracting value after decimal

text = "X-DSPAM-Confidence:    0.8475";
print float(text[text.find("0"):])

                 

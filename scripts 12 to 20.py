

# Code 12: reading a text file from working directory

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "Enter a valid file!"
    quit()
for line in fh:
    line=line.rstrip().upper()
    print line


# Code 13: string operations
fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid filename!"
    quit()
s=0
count=0
for line in fh:
    if not "X-DSPAM-Confidence" in line: continue
    x=line[line.find(":")+1:]
    x=float(x.rstrip())
    s=s+x
    count=count+1
avg=s/count
print "Average spam confidence:",avg

# Code 14: string operations

fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid file name!"
    exit()
final=list()
for line in fh:
    line=line.rstrip()
    x=line.split()
    for i in range(len(x)):
        word=x[i]
        if word in final: continue
        final.append(word)
final.sort()
print final

# Code 15: counting lines in a file starting with "From"
fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid file name!"
    exit()
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue
    x=line.split()
    print x[1]
    count=count+1
print "There were", count, "lines in the file with From as the first word"

# Code 16: using list, and dict

fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid file name!"
    exit()
d1=dict()
l1=list()
for line in fh:
    line=line.rstrip()
    if line.startswith("From "):
        x=line.split()
        l1.append(x[1])
for var in l1:
    d1[var]=d1.get(var,0)+1
email=None
count=None
for k,v in d1.items():
    if count is None:
        count=v
        email=k
    elif count < v:
        count=v
        email=k
print email,count
    
# Code 17: using list, and dict

fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid file name!"
    exit()
d1=dict()
l1=list()
l2=list()
for line in fh:
    line=line.rstrip()
    if line.startswith("From "):
        x=line.split()
        for y in x:
            if y.find(":") != -1:
                z=y.split(":")
                l1.append(z[0])
for var in l1:
    d1[var]=d1.get(var,0)+1
for k,v in d1.items():
    t=(k,v)
    l2.append(t)
l2.sort()
for z in l2:
    print z[0],z[1]
    
                
# Code 18: using regex in python
import re
fname=raw_input("Enter the file name: ")
try:
    fh=open(fname)
except:
    print "Enter a valid file name!"
    exit()
l1=list()
for line in fh:
    y=re.findall('[0-9]+', line)
    for x in y:
        l1.append(int(x))
print sum(l1)

# Code 19: accessing a web page 

import socket
firstsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
firstsock.connect(('data.pr4e.org', 80))
firstsock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
while True:
    data = firstsock.recv(512)
    if len(data) < 1: break
    print data
firstsock.close()


# Code 20: reading html using beautiful soup

import urllib
from BeautifulSoup import *

url=raw_input("Enter the URL - ")
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

# retrieve a list of "span" tags
# Each Tag is like a dictionary of HTML attributes

tags=soup("span")
sum=0
count=0
for tag in tags:
    x=tag.contents[0]
    if len(x) > 0:
        sum=sum+int(x)
        count=count+1
    else: continue
print count ,sum

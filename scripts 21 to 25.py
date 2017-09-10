# Code 21: Using urllib library 

import urllib
from BeautifulSoup import *
url=raw_input('Enter the URL - ')
try:
    html=urllib.urlopen(url).read()
except:
    print 'Enter a Valid URL'
    quit()
c=raw_input('Enter the number of times the process will repeat: ')
p=raw_input('Enter the position of the link: ')
l1=list()
while c > 0:
    soup=BeautifulSoup(html)
    tags=soup('a')
    for tag in tags:
        y=tag.get("href", None)
        l1.append(y)
    if len(l1) > p:
        html=urllib.urlopen(l1[p-1]).read()        
        print l1[p-1]
    else: 
        print 'URL does not contain ',p,' links'
        break
    l1=list()
    c=c-1
    
# Code 22: learning reading xml 

import urllib
import xml.etree.ElementTree as ET

loc=raw_input('Enter location')
print 'Retrieving', loc
try:
    xml=urllib.urlopen(loc).read()
except:
    print 'Enter valid url'
    quit()
print 'Retrieved',len(xml) ,'characters' 
tree=ET.fromstring(xml)
counts=tree.findall('.//count')
sum=0
c=0
for count in counts:
    x=count.text
    sum=sum+int(x)
    c=c+1
print 'Count:' ,c
print 'Sum:' ,sum

# Code 23: learning reading json 

import urllib
import json

loc=raw_input('Enter location')
print 'Retrieving', loc
try:
    js=urllib.urlopen(loc).read()
except:
    print 'Enter valid url'
    quit()
print 'Retrieved',len(js) ,'characters'
data=json.loads(str(js))
file=data['comments']
sum=0
c=0
for item in file:
    x=item['count']
    sum=sum+int(x)
    c=c+1
print 'Count:' ,c
print 'Sum:' ,sum


# Code 24: json another example

import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input('Enter location: ')
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
#print json.dumps(js, indent=4)
placeid= js['results'][0]['place_id']
print placeid

# Code 25: manipulating database using python

import sqlite3

conn = sqlite3.connect('domain.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
#if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    line=line.rstrip()
    pieces = line.split('@')
    domain = pieces[1].split()[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()


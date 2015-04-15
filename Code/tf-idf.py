import re
import sys
import math

point = [',', '.', '(', ')', '-', "'", '?', '!', '/', '\\', '%', '$', ':', '@', '=']
a = open('2001-2002.txt','r')
mysplit={}
mylist={}
myset = []
mynum = []
count = 0;
myabs = {}
for line in a:
	# for element in point:
	# 	line = line.replace(element, ' ')
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element,0)
		num = num + 1
		mylist[element] = num
	

for k,v in sorted(mylist.items(), key = lambda d:d[1]):
	print (k,v)
	print('\n')
totalnum = len(mylist)
a.close()
a = open('2011-2012.txt','r')
for line in a:
	count = 0;
	singlelist={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element,0)
		num = num + 1
		count += 1
		singlelist[element] = num
	mynum.append(count)
	myset.append(singlelist)

articlenum = len(myset)
i = 0

newset = []
for element in myset:
	
	newlist = {}
	for keyword in element:
		count = 0
		for node in myset:
			if(node.has_key(keyword)):
				count += 1
		idf = math.log(articlenum * 1.0/(count + 1))
		tf = 1.0 * element.get(keyword)/mynum[i]
		temp = newlist.setdefault(keyword, 0)
		newlist[keyword] = tf * idf * 1.0
	newset.append(newlist)
	i += 1

flag = 1
newlist = {}

for onelist in newset:
	
	# print('Abstract ')
	# print(flag)
	# print('\n')
	count = 0
	for k,v in sorted(onelist.items(), key = lambda d:d[1], reverse = True):
		print(k,v)
		num = newlist.setdefault(k, 0)
		num = num + 1
		newlist[k] = num
		count = count + 1
		if(count == 9):
			break
	flag += 1
# print count
count = 0
for k,v in sorted(newlist.items(), key = lambda d:d[1], reverse = True):
	print (k,v)
	if(count == 50):
		break
	count = count + 1
#print(len(mylist))

import re
import sys
import math

a = open('2001-2002.txt','r')
count = 0
mylist = {}
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()



a = open('2003-2004.txt','r')
count = 0
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()

a = open('2005-2006.txt','r')
count = 0
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()

a = open('2007-2008.txt','r')
count = 0
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()

a = open('2009-2010.txt','r')
count = 0
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()

a = open('2011-2012.txt','r')
count = 0
for line in a:
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = mylist.setdefault(element, -1)
		if(mylist[element] == -1):
			mylist[element] = len(mylist) - 1
	count = count + 1
	if(count == 1000):
		break
a.close()

for k,v in sorted(mylist.items(), key = lambda d:d[1], reverse = True):
	print (k,v)
# b = open('6index.txt', 'w')
mydict = {}
for k, v in mylist.items():
	mydict.setdefault(v, '')
	mydict[v] = k


b = open('1index.txt', 'w')
for k,v in sorted(mydict.items(), key = lambda d:d[0]):
	b.write(str(k))
	b.write(' ')
	b.write(v)
	b.write('\n')
b.close()

a = open('2001-2002.txt','r')
count = 0
flag = 1
b = open('dtm-mult.dat', 'w')
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')
		flag1 = flag1 + 1
	# print count,
	# for k,v in singlelist.items():
	# 	print repr(mylist[k]) + ':' + repr(v),
	# print ''
	flag = flag + 1
	if(flag == 1001):
		break
a.close()
b.write('\n')

a = open('2003-2004.txt','r')
count = 0
flag = 1
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')
		flag1 = flag1 + 1
	flag = flag + 1
	if(flag == 1001):
		break
a.close()
b.write('\n')

a = open('2005-2006.txt','r')
count = 0
flag = 1
# b = open('0506-mult.dat', 'w')
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')
		flag1 = flag1 + 1
	# print count,
	# for k,v in singlelist.items():
	# 	print repr(mylist[k]) + ':' + repr(v),
	# print ''
	flag = flag + 1
	if(flag == 1001):
		break
a.close()
b.write('\n')

a = open('2007-2008.txt','r')
count = 0
flag = 1
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')
		flag1 = flag1 + 1
	flag = flag + 1
	if(flag == 1001):
		break
a.close()
b.write('\n')

a = open('2009-2010.txt','r')
count = 0
flag = 1
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')
		flag1 = flag1 + 1
	flag = flag + 1
	if(flag == 1001):
		break
a.close()
b.write('\n')

a = open('2011-2012.txt','r')
count = 0
flag = 1
for line in a:
	count = 0
	singlelist = {}
	mysplit={}
	mysplit = line.split()
	for element in mysplit:
		element.strip()
		num = singlelist.setdefault(element, 0)
		num = num + 1
		singlelist[element] = num
		count = count + 1
	b.write(str(len(singlelist)))
	b.write(' ')
	flag1 = 1;
	for k,v in singlelist.items():
		b.write(str(mylist[k]))
		b.write(':')
		b.write(str(v))
		if(flag1 < len(singlelist)):
			b.write(' ')
		else:
			if(flag < 1000):
				b.write('\n')

		flag1 = flag1 + 1
	flag = flag + 1
	if(flag == 1001):
	 	break
a.close()
b.close()


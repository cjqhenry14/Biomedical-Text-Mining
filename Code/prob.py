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

# b = open('6index.txt', 'w')
mydict = {}
for k, v in mylist.items():
	mydict.setdefault(v, '')
	mydict[v] = k

count = 1

prob1 = {}
prob2 = {}
prob3 = {}
prob4 = {}
prob5 = {}
prob6 = {}
b = open('/Users/liuxichan/Desktop/dtm/example1/model_run/lda-seq/topic-009-var-e-log-prob.dat')
for line in b:
	# print line
	temp = (count - 1) % 527988
	flag = float(line)
	if((count / 527988.0) <= 1):
		prob1.setdefault(temp, 0)
		prob1[temp] = math.exp(flag)
	elif((count / 527988.0) <= 2):
		prob2.setdefault(temp, 0)
		prob2[temp] = math.exp(flag)
	elif((count / 527988.0) <= 3):
		prob3.setdefault(temp, 0)
		prob3[temp] = math.exp(flag)
	elif((count / 527988.0) <= 4):
		prob4.setdefault(temp, 0)
		prob4[temp] = math.exp(flag)
	elif((count / 527988.0) <= 5):
		prob5.setdefault(temp, 0)
		prob5[temp] = math.exp(flag)
	elif((count / 527988.0) <= 6):
		prob6.setdefault(temp, 0)
		prob6[temp] = math.exp(flag)

	count = count + 1
	# print count/527988
b.close()

b = open('0102/topic9.txt', 'w')
for k,v in sorted(prob1.items(), key = lambda d:d[1], reverse = True):
	b.write(str(k))
	b.write(' ')
	b.write(str(v))
	b.write('\n')
b.close()

# b = open('0104/0304/topic9.txt', 'w')
# for k,v in sorted(prob2.items(), key = lambda d:d[1], reverse = True):
# 	b.write(str(k))
# 	b.write(' ')
# 	b.write(str(v))
# 	b.write('\n')
# b.close()

# b = open('0106/0506/topic9.txt', 'w')
# for k,v in sorted(prob3.items(), key = lambda d:d[1], reverse = True):
# 	b.write(str(k))
# 	b.write(' ')
# 	b.write(str(v))
# 	b.write('\n')
# b.close()

# b = open('0108/0708/topic9.txt', 'w')
# for k,v in sorted(prob4.items(), key = lambda d:d[1], reverse = True):
# 	b.write(str(k))
# 	b.write(' ')
# 	b.write(str(v))
# 	b.write('\n')
# b.close()

# b = open('0108/0910/topic1.txt', 'w')
# for k,v in sorted(prob5.items(), key = lambda d:d[1], reverse = True):
# 	b.write(str(k))
# 	b.write(' ')
# 	b.write(str(v))
# 	b.write('\n')
# b.close()

# b = open('0108/1112/topic1.txt', 'w')
# for k,v in sorted(prob6.items(), key = lambda d:d[1], reverse = True):
# 	b.write(str(k))
# 	b.write(' ')
# 	b.write(str(v))
# 	b.write('\n')
# b.close()









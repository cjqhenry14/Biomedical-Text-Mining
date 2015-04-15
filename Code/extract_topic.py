import os

def get_topic(year_name):
	f = open('year_topic/top_5/' + year_name + '.twords', 'r')
	final_topic = open("final_topic/top_5/" + year_name + '.twords', 'a+')
	while 1:
		line = f.readline()
		#print line
		str_split = line.split(' ')

		if str_split[0] == "Topic":
			#print line,
			final_topic.write(line)
		else:
			#print str_split[0]
			final_topic.write(str_split[0] + '\n')

		if not line:
			break

	f.close()
	final_topic.close()

if (__name__ == '__main__'):
	get_topic('2001-2002')
	get_topic('2003-2004')
	get_topic('2005-2006')
	get_topic('2007-2008')
	get_topic('2009-2010')
	get_topic('2011-2012')
    









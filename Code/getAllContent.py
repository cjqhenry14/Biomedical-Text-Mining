#! /usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import os
from shutil import copyfile
import sys

def makeDir():
	root = 'author_content/MurrayChristopher/'
	#root = 'author_art/MurrayChristopher/'
	os.mkdir(root)
	os.mkdir(root + '2001-2002')
	os.mkdir(root + '2003-2004')
	os.mkdir(root + '2005-2006')
	os.mkdir(root + '2007-2008')
	os.mkdir(root + '2009-2010')
	os.mkdir(root + '2011-2012')

	'''os.mkdir(root + '2001-2004')
	os.mkdir(root + '2001-2006')
	os.mkdir(root + '2001-2008')
	os.mkdir(root + '2001-2010')
	os.mkdir(root + '2001-2012')'''


#get each document's content.
def getContent(year_name, xml_doc):
	f = open('author_content/MurrayChristopher/' + year_name + '/' + xml_doc, 'a+')
	soup = BeautifulSoup(open(os.path.join('author_art/MurrayChristopher/' + year_name, xml_doc)))
	for absTag in soup.find_all("art"):
		for content in absTag.find_all("p"):
			f.write(str(content.get_text()) + '\n')
	f.close()

#scan work dir to check each XML document.
def scanDir(year_name):
	file_list = os.listdir('author_art/MurrayChristopher/' + year_name)
	for xml_doc in file_list:
		if(xml_doc != '.DS_Store'):
			getContent(year_name, xml_doc)

if (__name__ == '__main__'):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	#makeDir()
	scanDir('2001-2002')
	scanDir('2003-2004')
	scanDir('2005-2006')
	scanDir('2007-2008')
	scanDir('2009-2010')
	scanDir('2011-2012')



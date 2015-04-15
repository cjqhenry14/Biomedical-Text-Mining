from bs4 import BeautifulSoup
import re
import os
num_array = [0, 0, 0, 0, 0, 0]
#Get desired fields from XML document.
def check(year, xml_doc):
    soup = BeautifulSoup(open(os.path.join('art_sample/' + year, xml_doc)))
    if (soup.art.fm.bibl.title == None):
        return

    pubdate = int(soup.art.fm.bibl.pubdate.string)

    if (pubdate <= 2002):
        num_array[0]+=1
    elif (pubdate > 2002 and pubdate <= 2004):
        num_array[1]+=1
    elif (pubdate > 2004 and pubdate <= 2006):
        num_array[2]+=1
    elif (pubdate > 2006 and pubdate <= 2008):
        num_array[3]+=1
    elif (pubdate > 2008 and pubdate <= 2010):
        num_array[4]+=1
    elif (pubdate > 2010 and pubdate <= 2012):
        num_array[5]+=1

def check_sample(year):
    file_list = os.listdir('art_sample/' + year)

    for xml_doc in file_list:
        if(xml_doc != '.DS_Store'):
            check(year, xml_doc)
    
if (__name__ == '__main__'):
    check_sample('2001-2002')
    check_sample('2003-2004')
    check_sample('2005-2006')
    check_sample('2007-2008')
    check_sample('2009-2010')
    check_sample('2011-2012')
    for index in range(len(num_array)):
        start = 2000 + index*2
        end = start + 2
        print start + 1, '-', end, ':', num_array[index]
    









from bs4 import BeautifulSoup
import re
import os
from shutil import copyfile
import random

num_array = [0, 0, 0, 0, 0, 0]
random.seed(3)
#Get desired fields from XML document.
def getFields(art_full_dir, xml_doc):
    soup = BeautifulSoup(open(os.path.join(art_full_dir, xml_doc)))
    if (soup.art.fm.bibl.title == None):
        return

    pubdate = soup.art.fm.bibl.pubdate.string
    divide_by_pubdate(art_full_dir, xml_doc, int(pubdate))

def divide_by_pubdate(art_full_dir, xml_doc, pubdate):
    if (pubdate <= 2002 and num_array[0] < 1000):
        num_array[0]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2001-2002', xml_doc))
    elif (pubdate > 2002 and pubdate <= 2004 and num_array[1] < 1000):
        num_array[1]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2003-2004', xml_doc))
    elif (pubdate > 2004 and pubdate <= 2006 and num_array[2] < 1000):
        num_array[2]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2005-2006', xml_doc))
    elif (pubdate > 2006 and pubdate <= 2008 and num_array[3] < 1000):
        num_array[3]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2007-2008', xml_doc))
    elif (pubdate > 2008 and pubdate <= 2010 and num_array[4] < 1000):
        num_array[4]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2009-2010', xml_doc))
    elif (pubdate > 2010 and pubdate <= 2012 and num_array[5] < 1000):
        num_array[5]+=1
        copyfile(os.path.join(art_full_dir, xml_doc), os.path.join('art_sample', '2011-2012', xml_doc))
    
def randomScanDir(year, art_full_dir):
    file_list = os.listdir(art_full_dir)
    if(year == '2001-2005'):
        xml_samples = random.sample(file_list, 10000)
        for xml_doc in xml_samples:
            if(num_array[0] == 1000):
                break
            if(xml_doc != '.DS_Store'):
                getFields(art_full_dir, xml_doc)

    if(year == '2006-2010'):
        xml_samples = random.sample(file_list, 3000)
        for xml_doc in xml_samples:
            if(num_array[2] == 1000):
                break
            if(xml_doc != '.DS_Store'):
                getFields(art_full_dir, xml_doc)

    if(year == '2011-2012'):
        xml_samples = random.sample(file_list, 1000)
        for xml_doc in xml_samples:
            if(xml_doc != '.DS_Store'):
                getFields(art_full_dir, xml_doc)

    
#before1999:0, [1999, 2000]=34
if (__name__ == '__main__'):
    randomScanDir('2001-2005', 'articles/2001-2005/large')
    #randomScanDir('2006-2010', 'articles/2006-2010/large')
    #randomScanDir('2011-2012', 'articles/2011-2012')

    for index in range(len(num_array)):
        start = 2000 + index*2
        end = start + 2
        print start + 1, '-', end, ':', num_array[index]









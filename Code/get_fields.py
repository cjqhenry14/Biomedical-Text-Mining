from bs4 import BeautifulSoup
import re
import os
from shutil import copyfile

author_set = set()
pubdate_set = set()
#Get desired fields from XML document.
def getFields(dir_name, xml_doc):
    soup = BeautifulSoup(open(os.path.join(dir_name, xml_doc)))
    if (soup.art.fm.bibl.title == None):
        return
    #title = soup.art.fm.bibl.title.p.string
    #for author_info in soup.find_all('au', id=re.compile("A\d+")):
    #    author_name = (str(author_info.snm), str(author_info.mnm), str(author_info.fnm))
    #    author_name_str = '.'.join(author_name)
    #    addAuthor(author_name_str)
    pubdate = soup.art.fm.bibl.pubdate.string
    divide_by_pubdate(dir_name, xml_doc, int(pubdate))

def divide_by_pubdate(dir_name, xml_doc, pubdate):
    if (pubdate <= 1975):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1969-1975', xml_doc))
    elif (pubdate <= 1980):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1976-1980', xml_doc))
    elif (pubdate <= 1985):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1981-1985', xml_doc))
    elif (pubdate <= 1990):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1986-1990', xml_doc))
    elif (pubdate <= 1995):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1991-1995', xml_doc))
    elif (pubdate <= 2000):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '1996-2000', xml_doc))
    elif (pubdate <= 2005):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '2001-2005', xml_doc))
    elif (pubdate <= 2010):
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '2006-2010', xml_doc))
    else:
        copyfile(os.path.join(dir_name, xml_doc), os.path.join(dir_name, '2011-2012', xml_doc))
def addAuthor(author_name_str):
    author_set.add(author_name_str)
def printAuthorList():
    for author in author_set:
        print (author)
#scan work dir to check each XML document.
def scanDir(dir_name):
    file_list = os.listdir(dir_name)
    for xml_doc in file_list:
        getFields(dir_name, xml_doc)

if (__name__ == '__main__'):
    #getFields('sample_articles/scrt51.xml')
    #scanDir('sample_articles')
    scanDir('articles')
    printAuthorList()

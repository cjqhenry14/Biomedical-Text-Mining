from bs4 import BeautifulSoup
import re
import os
from shutil import copyfile

Eugene_array = [0, 0, 0, 0, 0, 0]
Christopher_array = [0, 0, 0, 0, 0, 0]
year_array = ["2001-2002", "2003-2004", "2005-2006", "2007-2008", "2009-2010", "2011-2012"]
#Koonin Eugene   Murray Christopher
def get(year, xml_doc):
    #soup = BeautifulSoup(open(os.path.join('art_sample/' + year, xml_doc)))
    soup = BeautifulSoup(open(os.path.join('articles/' + year + "/large", xml_doc)))
    bible = soup.art.fm.bibl
    if (bible.aug == None):
        return

    pubdate = int(bible.pubdate.string)

    for name_tags in bible.aug.find_all("au"):
        if (name_tags.snm == None or name_tags.fnm == None):
            return
        s_name = name_tags.snm.string
        f_name = name_tags.fnm.string
        count_author_num(pubdate, s_name, f_name, xml_doc, year)
        #print s_name+'\n', f_name

def count_author_num(pubdate, s_name, f_name, xml_doc, year):
    if(pubdate == 2001 or pubdate == 2002):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[0]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[0] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[0]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[0] + "/" + xml_doc)
    #
    elif(pubdate == 2003 or pubdate == 2004):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[1]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[1] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[1]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[1] + "/" + xml_doc)
    #
    elif(pubdate == 2005 or pubdate == 2006):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[2]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[2] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[2]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[2] + "/" + xml_doc)
    #
    elif(pubdate == 2007 or pubdate == 2008):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[3]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[3] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[3]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[3] + "/" + xml_doc)
    #
    elif(pubdate == 2009 or pubdate == 2010):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[4]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[4] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[4]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[4] + "/" + xml_doc)
    #
    elif(pubdate == 2011 or pubdate == 2012):
        if(s_name=="Koonin"  and f_name=="Eugene"):
            Eugene_array[5]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/KooninEugene/" + year_array[5] + "/" + xml_doc)
        elif(s_name=="Murray"  and f_name=="Christopher"):
            Christopher_array[5]+=1
            copyfile("articles/" + year + "/large/" + xml_doc, "author_art/MurrayChristopher/" + year_array[5] + "/" + xml_doc)


def get_author_art(year):
    #file_list = os.listdir('art_sample/' + year)
    file_list = os.listdir('articles/' + year + '/large/')
    for xml_doc in file_list:
        if(xml_doc != '.DS_Store'):
            get(year, xml_doc)

if (__name__ == '__main__'):
    '''for index in range(len(year_array)):
        get_author_art(year_array[index])'''
    #get_author_art("2001-2005")
    #get_author_art("2006-2010")
    get_author_art("2011-2012")

    print "Eugene"
    for index in range(len(year_array)):
        print year_array[index], ':', Eugene_array[index]
    #
    print "Christopher"
    for index in range(len(year_array)):
        print year_array[index], ':', Christopher_array[index]
    









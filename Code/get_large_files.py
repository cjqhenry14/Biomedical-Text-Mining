import os
from shutil import copyfile

K = 200
def scanDir(dir_name):
    file_list = os.listdir(dir_name)
    os.mkdir(os.path.join(dir_name, 'large'))
    for cur_file in file_list:
        fp = open(os.path.join(dir_name, cur_file))
        line_count = len(fp.readlines())
        if (line_count > K):
            copyfile(os.path.join(dir_name, cur_file), os.path.join(dir_name, 'large', cur_file))

if (__name__ == '__main__'):
    scanDir('articles/1969-1975')
    scanDir('articles/1976-1980')
    scanDir('articles/1981-1985')
    scanDir('articles/1986-1990')
    scanDir('articles/1991-1995')
    scanDir('articles/1996-2000')
    scanDir('articles/2006-2010')


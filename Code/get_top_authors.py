def get_top_authors(fname, author_map_fname):
    K = 21
    fp = open(fname)
    author_map_fp = open(author_map_fname)
    author_map = {}
    for line in author_map_fp:
        line = line.replace('\n', '')
        author_name = line.split('\t')[0]
        if (line.split('\t')[1].isdigit()):
            author_ind = int(line.split('\t')[1])
            author_map[author_ind] = author_name
    for i, line in enumerate(fp):
        if (i >= K):
            break
        author_ind = int(line.split(' ')[0])
        print author_ind, author_map[author_ind]

if (__name__ == '__main__'):
    get_top_authors('weight_pr', 'author_index')

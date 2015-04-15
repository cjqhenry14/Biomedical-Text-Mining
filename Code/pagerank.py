import os
import math
N = 500000
ITER_COUNT = 300
DAMP_FAC = 0.85

#adj_table = [[0 for i in range(N)] for j in range (N)]
out_adj_list = [[] for i in range(N)]
in_adj_list = [[] for i in range(N)]
in_adj_count = [0 for i in range(N)]
out_adj_count = [0 for i in range(N)]
pr_table = [0.0 for i in range(N)]
prev_pr_table = [0.0 for i in range(N)]

auth = [1.0 for i in range(N)]
hub = [1.0 for i in range(N)]
prev_auth = [1.0 for i in range(N)]
prev_hub = [1.0 for i in range(N)]

def getHubAndAuthority(n):
    for step in range(ITER_COUNT):
        norm = 0.0
        for i in range(n):
            auth[i] = 0.0
            for j in range(in_adj_count[i]):
                v = in_adj_list[i][j]
                auth[i] += prev_hub[v]
            norm += auth[i] * auth[i]
        norm = math.sqrt(norm)
        for i in range(n):
            auth[i] /= norm

        norm = 0.0
        for i in range(n):
            hub[i] = 0.0
            for j in range(out_adj_count[i]):
                v = out_adj_list[i][j]
                hub[i] += prev_auth[v]
            norm += hub[i] * hub[i]
        norm = math.sqrt(norm)
        for i in range(n):
            hub[i] /= norm
        #printHubAndAuthority(n)
        copyTable(n, auth, prev_auth)
        copyTable(n, hub, prev_hub)

def initAdj(n):
    in_adj_count = out_adj_count = [0 for i in range(n)]
    #adj_table = [[0 for i in range(n)] for j in range(n)]
    in_adj_list = out_adj_list = [[] for i in range(n)]
    pr_table = prev_pr_table = [0.0 for i in range(n)]
    auth = prev_auth = [1.0 for i in range(n)]
    hub = prev_hub = [1.0 for i in range(n)]
def getAdjList(n):
    for i in range(n):
        for j in range(n):
            if (adj_table[i][j] == 1):
                out_adj_list[i].append(j)
                out_adj_count[i] += 1
                in_adj_list[j].append(i)
                in_adj_count[j] += 1
def printEdgeToFile(fname, n):
    fp = open(fname, 'w')
    for i in range(n):
        fp.write(str(i))
        adj_len = len(out_adj_list[i])
        for j in range(adj_len):
            adj_index = out_adj_list[i][j]
            fp.write(';' + str(adj_index))
        fp.write('\n')

def getAdjListFromFile(fname, n):
    fp = open(fname)
    for i, line in enumerate(fp):
        for j in line:
            out_adj_list[i].append(j)
            out_adj_count[i] += 1
            in_adj_list[j].append(i)
            in_adj_count[j] += 1
def addEdgeInList(u, v):
    out_adj_list[u].append(v)
    out_adj_count[u] += 1
    in_adj_list[v].append(u)
    in_adj_count[v] += 1
def addEdgeInTable(u, v):
    adj_table[u][v] = 1

def copyTable(n, source_table, dest_table):
    for i in range(n):
        dest_table[i] = source_table[i]
def printPageRank(n):
    for i in range(n):
        print i, pr_table[i]

def printHubAndAuthority(n):
    #for i in range(n):
    #    print hub[i],
    #print ''
    for i in range(n):
        print i, auth[i]
def getWeightedPageRank(n):
    for j in range(n):
        prev_pr_table[j] = 1.0
    #num of inlinks of all ref pages of a given page
    ref_in_count = [0 for i in range(n)]
    #num of outlinks of all ref pages of a given page
    ref_out_count = [0 for i in range(n)]
    for i in range(n):
        for j in range(out_adj_count[i]):
            adj_index = out_adj_list[i][j]
            ref_in_count[i] += in_adj_count[adj_index]
            ref_out_count[i] += out_adj_count[adj_index]
    for i in range(ITER_COUNT):
        for j in range(n):
            pr_table[j] = 0.0
            for k in range(in_adj_count[j]):
                adj_index = in_adj_list[j][k]
                #pr_table[j] += prev_pr_table[adj_index] / out_adj_count[adj_index]
                if ref_in_count[adj_index] != 0 and ref_out_count[adj_index] != 0:
                    pr_table[j] += prev_pr_table[adj_index] * \
                in_adj_count[j] / ref_in_count[adj_index] * out_adj_count[j] / ref_out_count[adj_index]
            pr_table[j] *= DAMP_FAC
            pr_table[j] += (1.0 - DAMP_FAC)
        #printPageRank(n)
        copyTable(n, pr_table, prev_pr_table)
#n is the num of vertices
def getPageRank(n):
    for j in range(n):
        prev_pr_table[j] = 1.0
    for i in range(ITER_COUNT):
        for j in range(n):
            pr_table[j] = 0.0
            for k in range(in_adj_count[j]):
                adj_index = in_adj_list[j][k]
                pr_table[j] += prev_pr_table[adj_index] / out_adj_count[adj_index]
            pr_table[j] *= DAMP_FAC
            pr_table[j] += (1 - DAMP_FAC)
        #print 'ITER COUNT: ', i
        #printPageRank(n)
        copyTable(n, pr_table, prev_pr_table)
def getPageRankFromFile(fname):
    fp = open(fname)
    n = 0
    for line in fp:
        n += 1
        line = line.replace('\n', '')
        splited_line = line.split(';')
        u = 0
        v = 0
        for i, node_id in enumerate(splited_line):
            if (i == 0):
                u = int(node_id)
            else:
                v = int(node_id)
            if (u != 260 and v != 260 and u != v and v != 0):
                addEdgeInList(u, v)
    #print n
    #getWeightedPageRank(n)
    getPageRank(n)
    printPageRank(n)
    #getHubAndAuthority(n)
    #printHubAndAuthority(n)
def testPageRank():
    n = 4
    initAdj(n)
    addEdgeInList(0, 1)
    addEdgeInList(0, 2)
    addEdgeInList(2, 0)
    addEdgeInList(1, 2)
    addEdgeInList(3, 2)
    getAdjList(n)
    #getWeightedPageRank(n)
    getHubAndAuthority(n)

title_to_author_map = dict()
author_to_index_map = dict()
class Doc:
    title = ''
    author_list = []
    cite_list = []
doc_list = []

def getPageRankForCite(fname):
    delim = '######@@@@@@'
    #0 for title, 1 for author, 2 for citations
    state = 0
    fp = open(fname)
    for line in fp:
        line = line.replace('\n', '')
        if (line == delim):
            state = (state + 1) % 3
            if (state == 0 and cur_doc.title != ''):
                doc_list.append(cur_doc)
        elif (state == 0):
            cur_doc = Doc()
            cur_doc.title = line
            cur_doc.author_list = []
            cur_doc.cite_list = []
        elif (state == 1):
            cur_doc.author_list.append(line)
        elif (state == 2):
            cur_doc.cite_list.append(line)
    doc_count = len(doc_list)
    diff_author_count = 0
    tot_author_count = 0
    for i in range(doc_count):
        title_to_author_map[doc_list[i].title] = doc_list[i].author_list
        tot_author_count += len(doc_list[i].author_list)
        for author in doc_list[i].author_list:
            if author not in author_to_index_map:
                author_to_index_map[author] = diff_author_count
                diff_author_count += 1
    for author in author_to_index_map:
        print author + '\t' + str(author_to_index_map[author])
    #print 'diff author count: ', diff_author_count
    #print 'total author count: ', tot_author_count
   # initAdj(doc_count)
   # for i in range(doc_count):
   #     cur_doc_author_list = doc_list[i].author_list
   #     for cite_title in doc_list[i].cite_list:
   #         if cite_title in title_to_author_map:
   #             cite_author_list = title_to_author_map[cite_title]
   #             for author1 in cur_doc_author_list:
   #                 for author2 in cite_author_list:
   #                     addEdgeInList(author_to_index_map[author1], author_to_index_map[author2])

   # printEdgeToFile('cite_graph', diff_author_count)
    #print 'doc count: ', doc_count
    #total_cite_count = 0
    #found_cite_count = 0
    #for i in range(doc_count):
    #    total_cite_count += len(doc_list[i].cite_list)
    #    for cite_title in doc_list[i].cite_list:
    #        if cite_title in title_to_author_map:
    #            found_cite_count += 1
    ##print 'total_cite_count: ', total_cite_count
    #print 'found_cite_count: ', found_cite_count

if (__name__ == '__main__'):
    #testPageRank()
    #getPageRankForCite('cite_info')
    getPageRankFromFile('cite_graph')

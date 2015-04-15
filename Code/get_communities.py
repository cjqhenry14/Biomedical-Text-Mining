community_index = {}
def get_communities(fname):
    max_community_id = 0
    fp = open(fname)
    for ind, line in enumerate(fp):
        if (ind == 0):
            continue
        splited_line = line.split(',')
        node_id = splited_line[0]
        modularity_class = int(splited_line[1])
        max_community_id = max(max_community_id, modularity_class)
        community_index[node_id] = modularity_class
    return max_community_id

def build_community_cite_graph(cite_graph_fname, max_community_id):
    cite_graph_fp = open(cite_graph_fname)
    community_graph_fp = []
    for i in range(max_community_id + 1):
        cur_community_graph_fname = 'community_' + str(i) + '.csv'
        cur_fp = open(cur_community_graph_fname, 'w')
        community_graph_fp.append(cur_fp)
    for line in cite_graph_fp:
        line = line.replace('\n', '')
        splited_line = line.split(';')
        cur_community_id = 0
        is_in_community = 1
        for ind, node_id in enumerate(splited_line):
            if ind == 0:
                if node_id not in community_index:
                    is_in_community = 0
                    break
                cur_community_id = community_index[node_id]
                community_graph_fp[cur_community_id].write(str(node_id))
            else:
                if ind not in community_index or community_index[node_id] != cur_community_id:
                    continue
                community_graph_fp[cur_community_id].write(';' + str(node_id) )
        if is_in_community:
            community_graph_fp[cur_community_id].write('\n')


if __name__ == '__main__':
    community_count = get_communities('modularity_class.csv')
    print community_count
    build_community_cite_graph('cite_graph', community_count)

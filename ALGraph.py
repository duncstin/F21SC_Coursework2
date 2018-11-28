from graphviz import Digraph
import re

class ShowDigraph:
    """Creates Digraph from a list of tuples, where tuples contain documents and a list of their readers"""

    def __init__(self, file):
        self.file = file

    def also_likes_graph(self, also_likes_list, doc_id, user_id=''):
        if also_likes_list:
            dot = Digraph(name="Also likes", node_attr={'shape': 'plaintext', 'fontsize': '16'}, strict=True)
            dot.format = 'ps'
            find = re.compile("_(.*?)_")
            try:  # attempt to get size of dataset from file name
                first = re.search(find, self.file).group(1)
                scale = "Size: " + first
            except AttributeError:  # set size as filename if size cannot be determined
                scale = self.file
            # create key to be shown on left of digraph
            dot.node('r', 'Readers')
            dot.node('d', 'Documents')
            dot.edge('r', 'd', label=scale)
            # create node distinguishing input document
            dot.node(doc_id[-4:], doc_id[-4:], shape='circle', color='green', style='filled', rank='d')
            # if a user id is specified, create distinguishing node and edge to input document
            if user_id != '':
                dot.node(user_id[-4:], user_id[-4:], shape='box', color='green', style='filled', rank='r')
                dot.edge(user_id[-4:], doc_id[-4:])
            for tup in also_likes_list:
                # create a node for document
                dot.node(tup[0][-4:], tup[0][-4:], shape='circle', rank='d')
                for reader in tup[1]:
                    # create node for reader, link reader to document & input document
                    dot.node(reader[-4:], reader[-4:], shape='box', rank='r')
                    dot.edge(reader[-4:], tup[0][-4:])
                    dot.edge(reader[-4:], doc_id[-4:])
            # print(dot.source)
            try:
                dot.render('test-output.gv', view=True)
            except:
                print("Close or rename output file")
        else:
            print('There are no "also likes" documents in the current data')

import json
import re
from graphviz import Digraph

class AlsoLikes:

    def __init__(self, filepath):
        self.file = filepath

    def get_file_generator(self, doc_id='', user_id=''):
        """Returns generator of all 'read' events in file. Filters by document id if provided"""
        f = open(self.file, "r", encoding='utf8')
        if doc_id == '' and user_id == '':
            for line in f:
                if re.search('"event_type":"read"', line):
                    yield line
        elif doc_id != '' and user_id == '':
            doc_string = '"subject_doc_id":"' + doc_id + '"'
            for line in f:
                if re.search('"event_type":"read"', line) and re.search(doc_string, line):
                    yield line
        elif user_id != '' and doc_id == '':
            user_string = '"visitor_uuid":"' + user_id + '"'
            for line in f:
                if re.search('"event_type":"read"', line) and re.search(user_string, line):
                    yield line
        else:
            print("cannot search doc_id and user id at the same time")


    def process_line(self, string_line, target):
        """Converts a string to json, returns target value from json"""
        json_line = json.loads(string_line)
        return json_line[target]

    def all_reader_docs(self, readers):
        """Returns dict, where keys are users and values are lists of docs they have read"""
        read_events = self.get_file_generator()
        reader_strings = self.convert_readers(readers)
        reader_docs = {}
        for reads in read_events:
            for tup in reader_strings:
                if re.search(tup[1], reads):
                    doc = self.process_line(reads, "subject_doc_id")
                    if tup[0] in reader_docs:
                        reader_docs[tup[0]].append(doc)
                    else:
                        reader_docs[tup[0]] = []
                        reader_docs[tup[0]].append(doc)
        return reader_docs


    def convert_readers(self, readers):
        """returns list of tuples containing user ids and verbose strings for searching in files."""
        verbose_readers = []
        for reader in readers:
            v_reader = '"visitor_uuid":"' + reader + '"'
            tup = (reader, v_reader)
            verbose_readers.append(tup)
        return verbose_readers

    def also_likes(self, doc_id, user_id='', sort=lambda x: sorted(x.items(), key=lambda k: len(k[1]), reverse=True)):
        readers_and_docs = self.get_readers_and_documents(doc_id, user_id)
        if user_id in readers_and_docs.keys():
            del readers_and_docs[user_id]
        docs_and_readers = self.invert_dict(readers_and_docs)
        if doc_id in docs_and_readers.keys():
            del docs_and_readers[doc_id]
        #sorted_by_value = sorted(docs_and_readers.items(), key=lambda kv: len(kv[1]))
        """freq = {}
        for k, v in docs_and_readers.items():
            freq[k] = len(v)"""
        return sort(docs_and_readers)[:10]

        print(docs_and_readers)
        """for key, value in readers_and_docs.items():
            for v in value:
                if v != doc_id:
                    if v in country_freq:
                        country_freq[v] += 1
                    else:
                        country_freq[v] = 1
        sorted = sort(country_freq)
        return sorted[0:10]"""


    def invert_dict(self, d):
        inverse = {}
        for key in d:
            # Go through the list that is saved in the dict:
            for item in d[key]:
                # Check if in the inverted dict the key exists
                if item not in inverse:
                    # If not create a new list
                    inverse[item] = [key]
                else:
                    inverse[item].append(key)
        return inverse

    def get_readers_and_documents(self, doc_id, user_id):
        file_as_generator = self.get_file_generator(doc_id)
        readers = []
        for line in file_as_generator:
            reader = self.process_line(line, "visitor_uuid")
            if reader:
                readers.append(reader)
        docs_for_readers = self.all_reader_docs(readers)
        return docs_for_readers

    #input = also_likes('sample_400k_lines.json', '140310171202-000000002e5a8ff1f577548fec708d50')
    #also_likes('sample_3M_lines.json', '140109173556-a4b921ab7619621709b098aa9de4d736')

    def also_likes_graph(self, doc_id, user_id=''):
        info = self.get_readers_and_documents(doc_id, user_id)
        dot = Digraph(name="Also likes", node_attr={'shape': 'plaintext', 'fontsize': '16'})
        # dot.format = 'ps'
        find = re.compile("_(.*?)_")
        try:
            first = re.search(find, self.file).group(1)
            scale = "Size: " + first
        except(AttributeError):
            scale = self.file
        dot.node('r', 'Readers')
        dot.node('d', 'Documents')
        dot.edge('r', 'd', label=scale)
        for key, value in info.items():
            distinct = set(value)
            if key == user_id:
                dot.node(key[-4:], key[-4:], shape='box', color='green', style='filled', rank='r')
                for d in distinct:
                    if d == doc_id:
                        dot.node(d[-4:], d[-4:], shape='circle', color='green', style='filled', rank='d')
                        dot.edge(key[-4:], d[-4:])
            else:
                dot.node(key[-4:], key[-4:], shape='box', rank='r')
                for d in distinct:
                    if d == doc_id:
                        dot.node(d[-4:], d[-4:], shape='circle', color='green', style='filled', rank='d')
                    else:
                        dot.node(d[-4:], d[-4:], shape='circle', rank='d')
                    dot.edge(key[-4:], d[-4:])
        print(dot.source)
        dot.render('test-output.gv', view=True)


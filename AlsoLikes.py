import re
from processfile import ProcessFile


class AlsoLikes(ProcessFile):
    """Class containing methods to implement an "also like" functionality"""

    def __init__(self, filepath):
        self.file = filepath
        super(AlsoLikes, self).__init__(self.file)

    def all_reader_docs(self, readers):
        """Returns dict, where keys are users and values are lists of docs they have read"""
        read_events = self.get_file_generator()
        reader_strings = self.convert_readers(readers)  # tuples pairing reader id with verbose version used for regex
        # ensures no "visitor_referrer" fields are mistakenly matched.
        reader_docs = {}
        for reads in read_events:
            for tup in reader_strings:
                if re.search(tup[1], reads):  # if the reader is in the yielded line
                    doc = self.process_line(reads, "subject_doc_id") # extract the document they have read
                    if tup[0] in reader_docs:  # if the reader is in the dictionary
                        reader_docs[tup[0]].append(doc)  # append the document they have read
                    else:  # reader not in dictionary
                        reader_docs[tup[0]] = []  # add reader
                        reader_docs[tup[0]].append(doc)  # append document they have read
        return reader_docs


    def convert_readers(self, readers):
        """returns list of tuples containing user ids and verbose strings for searching in files"""
        verbose_readers = []
        for reader in readers:
            v_reader = '"visitor_uuid":"' + reader + '"'  # construct verbose string used for regex.
            tup = (reader, v_reader)
            verbose_readers.append(tup)
        return verbose_readers

    def also_likes(self, doc_id, user_id='', sort=lambda x: sorted(x.items(), key=lambda k: len(k[1]), reverse=True)):
        """Returns list of tuples, containing document id and list of all users who have read it"""
        readers_and_docs = self.get_readers_and_documents(doc_id)
        if user_id in readers_and_docs.keys():  # remove user ID, so not recommending documents they have already read
            del readers_and_docs[user_id]
        docs_and_readers = self.invert_dict(readers_and_docs)
        if doc_id in docs_and_readers.keys(): # remove document ID, so not recommending the input document as an "also like" one
            del docs_and_readers[doc_id]
        return sort(docs_and_readers)[:10]  # only returns top 10 values

    def invert_dict(self, dictionary):
        """Inverts dict of lists to a new dict, where elements in lists are keys, and values are keys from old dict"""
        inverse = {}
        for key in dictionary:
            for item in dictionary[key]:
                if item not in inverse:
                    inverse[item] = [key]
                else:
                    inverse[item].append(key)
        return inverse

    def get_readers_and_documents(self, doc_id):
        """for a given input document, finds all readers, then all documents read by them.
        Returns dict where documents are keys and readers are in lists of values"""
        file_as_generator = self.get_file_generator(doc_id)  # all read events for given document
        readers = []
        for line in file_as_generator:  # iterate over those read events, collecting all readers for the document
            reader = self.process_line(line, "visitor_uuid")
            if reader:
                readers.append(reader)
        docs_for_readers = self.all_reader_docs(readers) # get all documents read by identified readers
        return docs_for_readers



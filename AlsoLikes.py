from processfile import ProcessFile


class AlsoLikes1(ProcessFile):

    file = ''
    user = ''

    def __init__(self, filepath):
        self.file = filepath
        super(AlsoLikes1, self).__init__(self.file)

    def also_likes(self, doc_id, user_id='', sort=lambda x: sorted(x.items(), key=lambda k: len(k[1]), reverse=True)):
        """Returns list of tuples, containing document id and list of all users who have read it"""
        read_events = self.get_file_generator()  # generator returning only read events
        docs_with_readers = self.get_docs_with_readers(read_events, doc_id, user_id)
        also_likes_dict = self.remove_input_doc(docs_with_readers, doc_id) # remove any documents read by the input user
        return sort(also_likes_dict)[:10]  #return top 10 sorted documents

    def get_docs_with_readers(self, lines, input_doc, input_user):
        """Gets list of readers who have read input document and dict of all documents containing list of readers"""
        readers = []
        documents = {}
        for reads in lines:
            reader = self.process_line(reads, "visitor_uuid")
            doc = self.process_line(reads, "subject_doc_id")
            if reader and (input_doc == doc):
                readers.append(reader)  # add readers to list who have read input document
            if doc not in documents:  # create dictionary of documents with list of all readers
                documents[doc] = [reader]
            else:
                documents[doc].append(reader)
        if input_user != '' and input_user not in readers:  # if input reader provided, ensure that it is valid
            input_user = ''
            print('Unrecognised input reader')
            self.user = input_user
        else:
            self.user = input_user
        return self.filter_dict(documents, readers, input_user)  # remove any documents that don't have readers who've read the input document

    def filter_dict(self, dictionary, list_of_targets, input_user=''):
        """Filter dictionary of lists to only include keys where the paired list of values is in a target list"""
        filtered = {}  # construct new dictionary to avoid deleting items while iterating
        for key, values in dictionary.items():
            for value in values:  # for each item in the list of values
                if value in list_of_targets and (value != input_user):  # keep value by adding to filtered dict
                    if key not in filtered:
                        filtered[key] = [value]  # add key, add value as list of 1
                    else:
                        if value not in filtered[key]:
                            filtered[key].append(value)  # add value to list for key
        return filtered

    def remove_input_doc(self, dictionary, input_doc):
        for k in list(dictionary.keys()):  # can't delete from dictionary you are iterating over
            if k == input_doc:
                del dictionary[k]
        return dictionary


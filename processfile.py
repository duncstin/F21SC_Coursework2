import json
import re


class ProcessFile:
    """Basic file processing superclass"""
    def __init__(self, file):
        self.file = file

    def get_file_generator(self, doc_id=''):
        """Returns generator of all 'read' events in file. Filters by document id if provided"""
        f = open(self.file, "r", encoding='utf8')
        if doc_id == '':  # if no document provided, only yield read events
            for line in f:
                if re.search('"event_type":"read"', line):
                    yield line
        else:  # if document provided, yield read events only for that document
            doc_string = '"subject_doc_id":"' + doc_id + '"'
            for line in f:
                if re.search('"event_type":"read"', line) and re.search(doc_string, line):
                    yield line


    def process_line(self, string_line, target):
        """Converts a string to json, returns target value from json"""
        regex = '\"' + str(target) + '\":\"(.*?)\"'
        re.compile(regex)
        return re.search(regex, string_line).groups(0)[0]

    def get_from_file(self, target_field, doc_id=''):
        """Users other methods in class to provide a frequency count for a given field. Filters for given document
        if provided"""
        relevant_lines = self.get_file_generator(doc_id)
        return self.count_frequency(target_field, relevant_lines)


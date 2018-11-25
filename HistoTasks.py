import json
import re
from CONSTANTS import cntry_to_cont as continent_converter, continents


class HistoTasks:

    file = ''

    def __init__(self, filepath):
        self.file = filepath

    def get_file_generator(self, file, doc_id=''):
        """Returns generator of all 'read' events in file. Filters by document id if provided"""
        f = open(file, "r", encoding='utf8')
        if doc_id == '':
            for line in f:
                if re.search('"event_type":"read"', line):
                    yield line
        else:
            doc_string = '"subject_doc_id":"' + doc_id + '"'
            for line in f:
                if re.search('"event_type":"read"', line) and re.search(doc_string, line):
                    yield line

    def process_line(self, string_line, target):
        """Converts a string to json, returns target value from json"""
        json_line = json.loads(string_line)
        return json_line[target]

    def count_frequency(self, target_field, generator):
        """Returns dictionary of frequencies of elements in a target field from a json string"""
        frequencies = {}
        for g in generator:
            target = self.process_line(g, target_field)
            if target in frequencies:
                frequencies[target] += 1
            else:
                frequencies[target] = 1
        return frequencies

    def get_from_file(self, target_field, doc_id=''):
        relevant_lines = self.get_file_generator(self.file, doc_id)
        return self.count_frequency(target_field, relevant_lines)

    def get_continents(self, countries):
        """Converts country frequency count to continent frequency count"""
        c = continents
        unrecognised = []
        for country in countries:
            try:
                c[continent_converter[country]] += countries[country]
            except:
                c['unknown'] += countries[country]
                unrecognised.append(country)
        print("unrecognised country codes:")
        print(unrecognised)
        return(c)

    def get_short_browser(self, browsers):
        short = {}
        find = re.compile("^[^/]*")
        for key, value in browsers.items():
            #print(key)
            #print(re.split("[ ]*/[ ]*", key)[1])
            first = re.search(find, key).group(0)
            if first in short:
                short[first] += value
            else:
                short[first] = value
        return short


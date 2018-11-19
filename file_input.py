import json
import pandas as pd



class FileInput:
    def __init__(self, filename):
        self.df = self.set_dataframe(filename)

    def set_dataframe(self, filename):
        input_as_list = self.input_file(filename)
        return self.create_dataframe(input_as_list)

    def input_file(self, filename):
        input_list = []
        with open(filename) as f:
            for line in f:
                current_line = self.process_line(json.loads(line))
                input_list.append(current_line)
        return input_list


    def process_line(self, line):
        desired_fields = ["visitor_uuid", "visitor_country", "visitor_useragent", "env_doc_id"]
        d = {}
        for field in desired_fields:
            if field in line:
                d[field] = line[field]
        return d

    def create_dataframe(self, data):
        table = pd.DataFrame.from_dict(data)
        table.rename(columns={'env_doc_id': 'doc_id', 'visitor_uuid': 'user_id', 'visitor_country': 'country',
                          'visitor_useragent': 'browser'}, inplace=True)
        return table

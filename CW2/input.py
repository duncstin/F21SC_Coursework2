import json
import pandas as pd


def input_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            current_line = process_line(json.loads(line))
            data.append(current_line)
    return data


def process_line(line):
    desired_fields = ["visitor_uuid", "visitor_country", "visitor_useragent", "env_doc_id"]
    d = {}
    for field in desired_fields:
        if field in line:
            d[field] = line[field]
    return d


print("\nExtracted relevant info")
data = input_file("issuu_sample.json")
for d in data:
    print(d)
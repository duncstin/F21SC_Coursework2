from processfile import *
from ALGraph import ShowDigraph
from decorator import timer

file = 'sample_100k_lines.json'
di = ShowDigraph(file)


def sort_descending(x):
    """Sorts dictionary by value, returning dict as list of tuples, highest first."""
    return sorted(x.items(), key=lambda k: k[1], reverse=True)

@timer
def also_likes():
    ps = ProcessFile(file)
    input_doc = "100806162735-00000000115598650cb8b514246272b5"
    input_user = '00000000deadbeef'
    readevents = ps.get_file_generator()
    readers = []
    documents = {}
    for reads in readevents:
        reader = ps.process_line(reads, "visitor_uuid")
        doc = ps.process_line(reads, "subject_doc_id")
        if reader and (input_doc == doc):
            readers.append(reader)
        if doc not in documents:
            documents[doc] = [reader]
        else:
            documents[doc].append(reader)
    print(readers)
    print(documents)

    """final = {}
    for key in list(documents.keys()):
        #if key == input_doc:
            #del documents[key]
        for values in list(documents.values()):
            for value in values:
                if value in readers:
                    print(value)
                    #del documents[key]
    print(documents)"""
    final = {}
    for key, values in documents.items():
        print(key)
        for value in values:
            if value in readers:
                if key not in final:
                    final[key] = [value]
                else:
                    if value not in final[key]:
                        final[key].append(value)
    print(final)
    for k in list(final.keys()):
        if k == input_doc:
            del final[k]

    for k, v in final.items():
        print(k)
        print(v)

    graph_input = sort_descending(final)
    di.also_likes_graph(graph_input, input_doc)

also_likes()

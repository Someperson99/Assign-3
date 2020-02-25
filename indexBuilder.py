# index builder
import re
from Posting import *
from corpus import *
from json_handler import *
import sys
"""
Simple in memory inverted index, based off of lectures
Does not have partial indexing yet
"""
def build_index():
    doc_num = 0
    mem_index_dict = dict()
    times_written_to_disk = 0
    url_dict = {}
    # TODO partial indexing, but don't need for milestone 1
        # while docs:
        #     batch = get_batch(docs)
    for i in get_all_jsons():
        print(i[0])
        doc_num = doc_num + 1
        if sys.getsizeof(mem_index_dict) >= 500000:
            write_to_file(mem_index_dict, times_written_to_disk)
            mem_index_dict.clear()
            times_written_to_disk += 1
        tokens = parse(i[1])
        for token in tokens:
            if token not in mem_index_dict:
                # WE ARE NOW USING LIST INSTEAD OF POSTING OBJECT
                mem_index_dict[token] = [[doc_num, 1]]   # [DOCID, COUNT]
            else:
                # if the current doc id is the same, update freqcount (no need to create new Posting object)
                if (mem_index_dict[token][-1])[0] == doc_num:
                    (mem_index_dict[token][-1])[1] = (mem_index_dict[token][-1])[1] + 1
                else:
                    mem_index_dict[token].append([doc_num, 1])
    write_to_file(mem_index_dict)


"""
Parsing text str to get a list of tokens.
    Reused from part 2 Assignment 2 
"""
def parse(text: str) -> list():
    data = []
    newList = []
    data = re.split('[^a-z]+', text.lower())
    data = list(filter(None, data))
    for i in data:
        newList.append(i)
    return newList

build_index()


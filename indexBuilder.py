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
        tokens = i[1].split()
        if len(tokens) > 5000:
            tokens = tokens[:50001]
        tokens = filter(parse, tokens)
        for token in tokens:
            if token.lower() not in mem_index_dict:
                # WE ARE NOW USING LIST INSTEAD OF POSTING OBJECT
                mem_index_dict[token.lower()] = [[doc_num, 1]]   # [DOCID, COUNT]
            else:
                # if the current doc id is the same, update freqcount (no need to create new Posting object)
                if (mem_index_dict[token.lower()][-1])[0] == doc_num:
                    (mem_index_dict[token.lower()][-1])[1] = (mem_index_dict[token.lower()][-1])[1] + 1
                else:
                    mem_index_dict[token.lower()].append([doc_num, 1])
    write_to_file(mem_index_dict, times_written_to_disk)


"""
Parsing text str to get a list of tokens.
    Reused from part 2 Assignment 2 
"""
def parse(text: str) -> bool:
    return re.match(r"[a-z|A-Z]+", text)

build_index()


# index builder
import re
from Posting import *
from corpus import *
from json_handler import *
import sys
import storePostings
"""
Simple in memory inverted index, based off of lectures
Does not have partial indexing yet
"""


def build_index():
    doc_num = 0
    mem_index_dict = dict()
    times_written_to_disk = 0
    url_dict = dict()
    for i in get_all_jsons():
        print(i[0])
        doc_num = doc_num + 1
        url_dict[doc_num] = (i[0], i[1][:180])
        if sys.getsizeof(mem_index_dict) >= 200000:
            # write_to_file(mem_index_dict, times_written_to_disk)
            storePostings.store_postings(mem_index_dict)
            mem_index_dict.clear()
            times_written_to_disk += 1

        tokens = parse(i[1] + " " + i[2])
        for token in tokens:
            if token.lower() not in mem_index_dict:
                # WE ARE NOW USING LIST INSTEAD OF POSTING OBJECT
                mem_index_dict[token.lower()] = [[doc_num, 1]]  # [DOCID, COUNT]
            else:
                # if the current doc id is the same, update freqcount (no need to create new Posting object)
                if (mem_index_dict[token.lower()][-1])[0] == doc_num:
                    (mem_index_dict[token.lower()][-1])[1] = (mem_index_dict[token.lower()][-1])[1] + 1
                else:
                    mem_index_dict[token.lower()].append([doc_num, 1])
    storePostings.store_postings(mem_index_dict)
    with open('C:\\Users\\geryj\\Documents\\Index Copy\\urldict.json', 'w') as file:
        json.dump(url_dict, file)
    file.close()



"""
Parsing text str to get a list of tokens.

"""
def parse(word: str) -> list:
    """ takes in a string that might not be valid,
    so separate by alpha numeric, returns a list of new tokens"""
    result = list()
    tempWord = ""
    for char in word:
        if char.isalnum():
            tempWord += char
        else:
            if tempWord != '':
                if len(result) > 3000:
                    return result
                result.append(tempWord.lower())
                tempWord = ""
    if tempWord != "":
        result.append(tempWord.lower())
    return result


build_index()

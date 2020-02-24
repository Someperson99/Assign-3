# index builder
import re
from Posting import *
from corpus import *
"""
Simple in memory inverted index, based off of lectures
Does not have partial indexing yet
"""
def build_index():
    doc_num = 0
    mem_index_dict = dict()
    # TODO partial indexing, but don't need for milestone 1
        # while docs:
        #     batch = get_batch(docs)
    for i in get_all_jsons():
        doc_num = doc_num + 1
        if doc_num % 10 == 0:
            print(mem_index_dict)
            asdf = input()
            # yield mem_index_dict
        tokens = parse(i[1])
        for token in tokens:
            if token not in mem_index_dict:
                #if a token is not in the index
                mem_index_dict[token] = [Posting(doc_num, 1)]
            else:
                # if the current doc id is the same, update freqcount (no need to create new Posting object)
                if (mem_index_dict[token][-1]).docid == doc_num:
                    # (mem_index_dict[token][-1]).tfidf = (mem_index_dict[token][-1]).tfidf + 1
                    (mem_index_dict[token][-1]).tfidf += 1
                else:
                    mem_index_dict[token].append(Posting(doc_num, 1))


"""
Parsing text str to get a list of tokens.
    Reused from part 2 Assignment 2 @miKeEt
"""
def parse(text: str) -> list():
    data = []
    newList = []
    data = re.split('[^a-z]+', text.lower())
    data = list(filter(None, data))
    for i in data:
        newList.append(i)
    return newList

if __name__ == "__main__":
    build_index()

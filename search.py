import os
from json_handler import get_json_content
from time import time
import string
import math
import storePostings
import json
from collections import OrderedDict


def get_postings(word:str) -> list:
    '''given a word this function will find all postings from the index, assuming
    it has already been created'''
    if ("AND" in word or " "):
        query = word.replace(" AND", "").lower().split()
    else:
        query = [word.lower()]

    res = []

    #for each token in the query
    for token in query:
        #retrieve all of the postings, put it into a list, and then
        #put it into res
        res.append(storePostings.get_postings(token))

    return res

    # first_letter = list(q[0] for q in query)
    # index = 0
    # current_dir = os.getcwd()
    # all_postings = []
    # for letter in first_letter:
    #     num = 0
    #     postings = []
    #     target_path = current_dir + "/" + letter + str(num) + ".json"
    #     valid_path = os.path.exists(target_path)
    #     while valid_path:
    #         json_content = get_json_content(current_dir + "/" + letter + str(num) + ".json")
    #         if query[index] in json_content:
    #             for t in json_content[query[index]]:
    #                 postings.append((t[0], t[1]))
    #         num += 1
    #         valid_path = os.path.exists(current_dir + "/" + letter + str(num) + ".json")
    #     index += 1
    #     all_postings.append(postings)
    # return all_postings

def merge_postings(all_postings: list) -> list:
    # need all_postings to be a list of lists of tuples
    all_postings.sort(key = len)
    t = {}
    for posting in all_postings[0]:
        #this is dealing with only one list so posting
        #is a string representation of a post, eg. '13:3'
        #so that's why we have to split it
        post = posting.split(':')
        if not len(post) == 1:
            docID = int(post[0])
            frequency = int(post[1])
            t[docID] = frequency
    # print(t, "this is t\n")
    # t = dict(all_postings[0])
    for postings in all_postings[1:]:
        #for the other lists that are in postings...
        temp = {}
        for posting in postings:
            #doing the same thing here, just getting all of
            #the posting information and putting it into
            #temp
            post = posting.split(':')
            if not len(post) == 1:
                docID = int(post[0])
                frequency = int(post[1])
                temp[docID] = frequency
        # print(temp, "this is temp\n")
        result = {}
        #put all of the keys into a set, and compare them to
        #t which holds the shortest amount of keys
        match = set(temp.keys()).intersection(t.keys())
        for key in match:
            #add the postings that match up into result
            result[key] = temp[key] + t[key]
        t = result.copy()
    # print(len(result))
    return result

x1 = time()
print(merge_postings(get_postings("cristina machine learning")))
x2 = time()

print(x2-x1)

def get_tfidf(postings_dict: dict) -> dict:
    """ get tfidf score given a word AT SEARCH TIME
        The tf-idfweight of a term is the product of its tfweight and its idfweight.
        wt,d= (1+log(tft,d)) x log(N/dft)
    """
    #dictionary that will hold the docID as the key, and tf*idf as its value
    tfidf = dict()
    #over here we are just opening up the json file that contains all of the docIDs
    #and extracting the largest docID from it, this will represent the number of files
    #since the docID is essentially a counter of documents
    with open("C:\\Users\\geryj\\Documents\\Index Copy\\urldict.json", 'r') as f:
        res = json.load(f)
        f.close()
    num_documents = int(list(res.keys())[-1])
    # for i in string.ascii_lowercase:
    #     target_path = current_dir + "/" + i + str(num) + ".json"
    #     valid_path = os.path.exists(target_path)
    #     while valid_path:
    #         json_content = get_json_content(current_dir + "/" + i + str(num) + ".json")
    #         for word in json_content:
    #             if int(json_content[word][-1][0]) > num_documents:
    #                 num_documents = int(json_content[word][-1][0])
    #         num += 1
    #         valid_path = os.path.exists(current_dir + "/" + i + str(num) + ".json")

    document_frequency = len(postings_dict)  # num of documents that contain token
    idf = math.log((num_documents / document_frequency), 10)
    for key in postings_dict.keys():
        tfidf[key] = (1 + math.log(postings_dict[key], 10)) * idf
    return tfidf


x3 = time()
print(sorted(get_tfidf(merge_postings(get_postings("cristina machine learning"))).items(), key=lambda kv: kv[1], reverse=True))
x4 = time()
print(x4-x3)
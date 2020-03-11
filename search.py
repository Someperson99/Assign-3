import os
from json_handler import get_json_content
from time import time
import string
import math
from collections import OrderedDict


def get_postings(word:str) -> list:
    '''given a word this function will find all postings from the index, assuming
    it has already been created'''
    if ("AND" in word or " "):
        query = word.replace(" AND", "").lower().split()
    else:
        query = [word.lower()]
    first_letter = list(q[0] for q in query)
    index = 0
    current_dir = os.getcwd()
    all_postings = []
    for letter in first_letter:
        num = 0
        postings = []
        target_path = current_dir + "/" + letter + str(num) + ".json"
        valid_path = os.path.exists(target_path)
        while valid_path:
            json_content = get_json_content(current_dir + "/" + letter + str(num) + ".json")
            if query[index] in json_content:
                for t in json_content[query[index]]:
                    postings.append((t[0], t[1]))
            num += 1
            valid_path = os.path.exists(current_dir + "/" + letter + str(num) + ".json")
        index += 1
        all_postings.append(postings)
    return all_postings

def merge_postings(all_postings: list) -> list:
    # need all_postings to be a list of lists of tuples
    all_postings.sort(key = len)
    t = dict(all_postings[0])
    for postings in all_postings[1:]:
        temp = dict(postings)
        result = {}
        match = set(temp.keys()).intersection(t.keys())
        for key in match:
            result[key] = temp[key] + t[key]
        t = result.copy()
    print(len(result))
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
    tfidf = dict()
    current_dir = os.getcwd()
    num = 0
    num_documents = 0
    for i in string.ascii_lowercase:
        target_path = current_dir + "/" + i + str(num) + ".json"
        valid_path = os.path.exists(target_path)
        while valid_path:
            json_content = get_json_content(current_dir + "/" + i + str(num) + ".json")
            for word in json_content:
                if int(json_content[word][-1][0]) > num_documents:
                    num_documents = int(json_content[word][-1][0])
            num += 1
            valid_path = os.path.exists(current_dir + "/" + i + str(num) + ".json")

    document_frequency = len(postings_dict)  # num of documents that contain token
    idf = math.log((num_documents / document_frequency), 10)
    for key in postings_dict.keys():
        tfidf[key] = (1 + math.log(postings_dict[key], 10)) * idf
    return tfidf


x3 = time()
print(sorted(get_tfidf(merge_postings(get_postings("cristina machine learning"))).items(), key=lambda kv: kv[1], reverse=True))
x4 = time()
print(x4-x3)
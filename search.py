import os
from json_handler import get_json_content
from time import time
import string
import math


def get_postings(word:str) -> list:
    '''given a word this function will find all postings from the index, assuming
    it has already been created'''
    first_letter = word[0]
    num = 0
    current_dir = os.getcwd()
    target_path = current_dir + "/" + first_letter + str(num) + ".json"
    all_postings = []
    valid_path = os.path.exists(target_path)
    while valid_path:
        json_content = get_json_content(current_dir + "/" + first_letter + str(num) + ".json")
        if word in json_content:
            all_postings.extend(json_content[word])
        num += 1
        valid_path = os.path.exists(current_dir + "/" + first_letter + str(num) + ".json")

    return all_postings

x1 = time()
print(get_postings("science"))
x2 = time()

print(x2-x1)


def get_tfidf(postings_list: list) -> dict:
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

    document_frequency = len(postings_list)  # num of documents that contain token
    idf = math.log((num_documents / document_frequency), 10)
    for (docID, freq) in postings_list:
        tfidf[docID] = (1 + math.log(freq, 10)) * idf
    return tfidf


x3 = time()
print(sorted(get_tfidf(get_postings("science")).items(), key=lambda kv: kv[1], reverse=True))
x4 = time()
print(x4-x3)

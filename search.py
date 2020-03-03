import os
from json_handler import get_json_content
from time import time
import string
import math



def get_postings(word: str) -> list:
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
        target_path = current_dir + "/results/" + letter + str(num) + ".json"
        valid_path = os.path.exists(target_path)
        while valid_path:
            json_content = get_json_content(current_dir + "/results/" + letter + str(num) + ".json")
            if query[index] in json_content:
                postings.extend(json_content[query[index]])
            num += 1
            valid_path = os.path.exists(current_dir + "/results/" + letter + str(num) + ".json")
        index += 1
        all_postings.append(postings)
    return all_postings


def merge_postings(all_postings: list) -> list:
    shortest = {}
    all_postings.sort(key=len)
    x = 1
    for postings in all_postings[0]:
        shortest[postings[0]] = postings[1]
    if len(all_postings) < 2:
        return shortest
    t = {}
    for postings in all_postings[1:]:
        temp = {}
        result = {}
        for post in postings:
            temp[post[0]] = post[1]
        if x == 1:
            for key in shortest.keys():
                if key in temp.keys():
                    result[key] = shortest[key] + temp[key]
        else:
            for key in t.keys():
                if key in temp.keys():
                    result[key] = t[key] + temp[key]
        for key in result.keys():
            t[key] = result[key]
        x += 1
        if x >= len(all_postings):
            print(len(result))
            return result


x1 = time()
print(merge_postings(get_postings("master of software engineering")))
x2 = time()

print(x2 - x1)


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
        target_path = current_dir + "/results/" + i + str(num) + ".json"
        valid_path = os.path.exists(target_path)
        while valid_path:
            json_content = get_json_content(current_dir + "/results/" + i + str(num) + ".json")
            for word in json_content:
                if int(json_content[word][-1][0]) > num_documents:
                    num_documents = int(json_content[word][-1][0])
            num += 1
            valid_path = os.path.exists(current_dir + "/results/" + i + str(num) + ".json")

    document_frequency = len(postings_dict)  # num of documents that contain token
    idf = 0
    if document_frequency > 0:
        idf = math.log((num_documents / document_frequency), 10)
    for key in postings_dict.keys():
        tfidf[key] = (1 + math.log(postings_dict[key], 10)) * idf
    return tfidf





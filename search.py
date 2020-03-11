import math
import storePostings
import json

#depending on where you have urldict.json stored, you're going
#to want to change this
path = "C:\\Users\\geryj\\Documents\\Index Copy\\"

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

def merge_postings(all_postings: list) -> list:
    # need all_postings to be a list of lists of tuples
    result = {}
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
    if len(all_postings) == 1: return t
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
        #put all of the keys into a set, and compare them to
        #t which holds the shortest amount of keys
        match = set(temp.keys()).intersection(t.keys())
        for key in match:
            #add the postings that match up into result
            result[key] = temp[key] + t[key]
        t = result.copy()
    return result

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
    with open(path + "urldict.json", 'r') as f:
        res = json.load(f)
        f.close()
    num_documents = int(list(res.keys())[-1])

    document_frequency = len(postings_dict)  # num of documents that contain token
    idf = math.log((num_documents / document_frequency), 10)
    for key in postings_dict.keys():
        tfidf[key] = (1 + math.log(postings_dict[key], 10)) * idf
    return tfidf

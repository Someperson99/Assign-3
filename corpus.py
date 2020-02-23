import os
import os.path
import json
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import string  
import sys
import operator
import re
from urllib.parse import urlparse

from indexBuilder import Posting
def get_subdirectory_paths() -> list:
    '''function will prompt users to put in path of DEV so that
    all of the subfolders of DEV which represent subdomains can be
    presented as paths'''
    corpus_path = input()
    sub_domains = [i.path for i in os.scandir(corpus_path) if i.is_dir() and ".idea" not in i.path]
    return sub_domains


def read_json_files(path: str) -> str:
    '''given a path to a json file, the funtion will read the json file and return
    the url of the json file as well as the content from the url in a tuple'''
    f = open(path, 'r')
    html_data = json.load(f)
    f.close()
    return (html_data['url'], html_data['content'])

def get_all_jsons() -> dict:
    '''generator function that will yield a site's json information after
    going through each subdomain'''
    sub_domains = get_subdirectory_paths()

    for sub_domain in sub_domains:
        json_paths = [i for i in os.listdir(sub_domain)]
        for site in json_paths:
            yield read_json_files(sub_domain + "\\" + site)


# not sure to remove the stop word or leave it 
def tokenize_without_stopwords(text : "str") -> list:
    data = []
    newList = []
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    data = re.split('[^a-z]+',text.lower())
    data = list(filter(None, data))
    for i in data:
        if i not in stop_words:
            newList.append(i)
    #c = set(data) - set(stop_words)   list(c)
    return newList
def computeWordFrequencies(lst : list ) -> dict:
    d = dict()
    for token in lst:
        if token in d:
            d[token] += 1 
        else:
            d[token] = 1
    
    return d




"""  
Main starts here 
it will print the list of tuples 
"""
doc_id = 0
freq = 0

beautiful_list = []  #--> list of tuples that goes to the disc
dic_memory = dict()  # --> stays in mem (docId, url)
for i in get_all_jsons():
    index_dic = dict()
    lst = []

    soup = BeautifulSoup(i[1], features="html.parser")
    title = soup.title.string.strip()
    content = ""
    for para in soup.find_all('p'):
        content += str(para.text)
    content = title + content
    lst = tokenize_without_stopwords(content)
    # To do positon i need to iterate throough list just to get position
    dict_temp = dict()
    dict_temp = computeWordFrequencies(lst)
    for d in dict_temp:
        freq = dict_temp[d]
        myObj = Posting(doc_id,freq)
        index_dic[d] = myObj
        # not add the dictioanry with key value(docId, position) to beautiful_list
        beautiful_list.append(index_dic)
    print(beautiful_list)

    # End of iteration
    doc_id += 1  # --> docId iteration

    # might need to add the counter of 10 or less 
    print(beautiful_list)

    asdf = input()
# C:\Users\mikeb\Desktop\Assign-3\developer\DEV

import os
import os.path
import json
from bs4 import BeautifulSoup


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
    soup = BeautifulSoup(html_data['content'], features='html.parser')
    try:
        title = soup.title.string.strip()
    except:
        title = ""

    content = soup.get_text(strip=True)

    return (html_data['url'], title + content)

def get_all_jsons() -> dict:
    '''generator function that will yield a site's json information after
    going through each subdomain'''
    sub_domains = get_subdirectory_paths()

    for sub_domain in sub_domains:
        json_paths = [i for i in os.listdir(sub_domain)]
        for site in json_paths:
            yield read_json_files(sub_domain + "/" + site)

# for i in get_all_jsons():
#     print(i)
#     asd = input()


# sub_domain_jsons =  {   sub_domain_key : [  json_file1, json_file2, ....]
#                     }
#
#
# json_file1 = {url: ics.uci.edu, content: html_content}
#
# inv_index { word: doc1, doc2, ...
#             word2: doc 3, doc1}
#
# inv_index2 = {0, ics.uci.edu,
#               1, stat.uci.edu}
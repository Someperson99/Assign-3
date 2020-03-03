import os
import os.path
import json
from bs4 import BeautifulSoup



def get_subdirectory_paths(path = "") -> list:
    '''function will prompt users to put in path of DEV so that
    all of the subfolders of DEV which represent subdomains can be
    presented as paths'''
    if path != "":
        corpus_path = path
    else:
        corpus_path = input()
    invalid = True
    while invalid:
        if os.path.isdir(corpus_path):
            invalid = False
            break
        print("Invalid path, please try again")
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

    content = ""
    for para in soup.find_all('p'):
        content += str(para.text)

    # LETS SAVE TITLE SEPARATELY SO WE CAN USE IT FOR THE GUI <3
    return (html_data['url'], title, content)

def get_all_jsons() -> dict:
    '''generator function that will yield a site's json information after
    going through each subdomain'''
    sub_domains = get_subdirectory_paths()

    for sub_domain in sub_domains:
        json_paths = [i for i in os.listdir(sub_domain)]
        for site in json_paths:
            yield read_json_files(sub_domain + "/" + site)



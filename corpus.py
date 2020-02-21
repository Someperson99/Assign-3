import os
import os.path
import json


def get_subdirectory_paths() -> list:
    '''function will prompt users to put in path of DEV so that
    all of the subfolders of DEV which represent subdomains can be
    presented as paths'''
    corpus_path = input()
    sub_domains = [i.path for i in os.scandir(corpus_path) if i.is_dir() and ".idea" not in i.path]
    return sub_domains


def read_json_files(path: str) -> str:
    '''given a path to a json file, the funtion will read the json file and return
    the json as a string'''
    f = open(path, 'r')
    html_data = f.readline()
    f.close()
    return html_data

def get_all_jsons() -> dict:
    '''generator function that will yield a site's json information after
    going through each subdomain'''
    sub_domains = get_subdirectory_paths()
    sub_domain_jsons = {}
    site_jsons = []

    for sub_domain in sub_domains:
        sub_domain_key = sub_domain.split('\\')[-1]
        json_paths = [i for i in os.listdir(sub_domain)]
        for site in json_paths:
            site_jsons.append(read_json_files(sub_domain + "\\" + site))
        sub_domain_jsons[sub_domain_key] = site_jsons
        yield sub_domain_jsons
        sub_domain_jsons = {}




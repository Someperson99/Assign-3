import os
from json_handler import get_json_content
from time import time

def get_postings(word:str) -> list:
    '''given a word this function will find all postings from the index, assuming
    it has already been created'''
    first_letter = word[0]
    num = 0
    current_dir = os.getcwd()
    target_path = current_dir + "\\" + first_letter + str(num) + ".json"
    all_postings = []
    valid_path = os.path.exists(target_path)
    while valid_path:
        json_content = get_json_content(current_dir + "\\" + first_letter + str(num) + ".json")
        if word in json_content:
            all_postings.extend(json_content[word])
        num += 1
        valid_path = os.path.exists(current_dir + "\\" + first_letter + str(num) + ".json")

    return all_postings


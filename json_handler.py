import json
import os

def create_json_file(letter: str, index: dict):
    '''given a starting letter and an index this function will create a
    json file nammed after the letter parameter and insert the index
    parameter into the json file'''
    with open(letter+'.json', 'w') as file:
        json.dump(index, file)
    file.close()

def get_json_content(path:str) -> dict:
    '''given a path to a json file this function will return the
    json data in dictionary form'''
    f = open(path, 'r')
    index = json.load(f)
    f.close()
    return index


def write_to_file(index: dict):
    curr_dir = os.getcwd()
    letter_dict = {}
    curr_letter = ""
    #temporary dictionary that will store all the words that start with a certain letter
    for i in sorted(index.keys()):
        first_letter = i[0]
        if curr_letter == "":
            curr_letter = first_letter
        elif curr_letter == first_letter:
            letter_dict[i] = index[i]
        else:
            # if not os.path.exists(curr_dir + "\\" + first_letter + ".json"):
            #     create_json_file(first_letter, letter_dict)
            if os.path.exists(curr_dir + "\\" + first_letter + ".json"):
                prev_index = get_json_content(curr_dir + "\\" + first_letter + ".json")
                prev_index.update(letter_dict)
                letter_dict = prev_index
            create_json_file(first_letter, letter_dict)
            curr_letter = i[0]
            letter_dict = {}




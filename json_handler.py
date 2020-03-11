import json
import os


def create_json_file(letter: str, index: dict, version: int):
    '''given a starting letter and an index this function will create a
    json file nammed after the letter parameter and insert the index
    parameter into the json file'''
    with open("/Users/allysonyamasaki/PycharmProjects/Assign-3/results/"+letter + str(version) +  '.json', 'w') as file:
        json.dump(index, file)
    file.close()


def get_json_content(path: str) -> dict:
    '''given a path to a json file this function will return the
    json data in dictionary form'''
    f = open(path, 'r')
    index = json.load(f)
    f.close()
    return index


def write_to_file(index: dict, times_written_to_disk: int):
    curr_dir = os.getcwd()
    letter_dict = {}
    curr_letter = ""
    # temporary dictionary that will store all the words that start with a certain letter
    for i in sorted(index.keys()):
        first_letter = i[0]
        if curr_letter == "":
            curr_letter = first_letter
        elif curr_letter == first_letter:
            pass
        else:

            """
            MAC USERS:

            if os.path.exists(curr_dir + "/" + first_letter + ".json"):
                prev_index = get_json_content(curr_dir + "/" + first_letter + ".json")
            """

            create_json_file(curr_letter, letter_dict, times_written_to_disk)
            curr_letter = i[0]
            letter_dict = {}
        letter_dict[i] = index[i]

    if curr_letter == "z":
        create_json_file(curr_letter, letter_dict, times_written_to_disk)




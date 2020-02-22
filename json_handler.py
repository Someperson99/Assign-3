import json

def create_json_file(word_info: dict):
    first_character = word_info[0].lower()
    with open(first_character+'.json', 'w') as file:
        json.dump(test_dict, file)


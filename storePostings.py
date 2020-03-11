import os

def store_postings(postings_dict: dict):
    for word, postings in postings_dict.items():
        path = word + ".txt"
        if not os.path.exists(word + ".txt"):
            f = open(word + ".txt", 'w')
            f.close()
        postings_str = ""
        for posting in postings:
            postings_str += str(posting[0]) + ":" + str(posting[1]) + ","
        with open(path, 'a') as f:
            f.write(postings_str)


def get_postings(word: str):
    with open(word + ".txt", 'r') as f:
        return f.readline()
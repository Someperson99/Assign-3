import os

def store_postings(postings_dict: dict):
    for word, postings in postings_dict.items():
        print(word)
        path = "C:\\Users\\geryj\Documents\\Index Copy\\"
        if not os.path.exists(path + word + ".txt"):
            f = open(path + word + ".txt", 'w')
            f.close()
        postings_str = ""
        for posting in postings:
            postings_str += str(posting[0]) + ":" + str(posting[1]) + ","
        with open(path + word, 'a') as f:
            f.write(postings_str)


def get_postings(word: str):
    with open(word + ".txt", 'r') as f:
        res = f.readline().split()
    f.close()
    return res
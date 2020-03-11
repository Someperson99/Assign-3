
def store_postings(postings_dict: dict):
    for word, postings in postings_dict.items():
        path = "C:\\Users\\geryj\Documents\\Index Copy\\"
        file_name = word + ".txt"
        postings_str = ""
        for posting in postings:
            postings_str += str(posting[0]) + ":" + str(posting[1]) + ","
        try:
            f = open(path + file_name, 'a')
        except:
            pass
        else:
            f.write(postings_str)
            f.close()


def get_postings(word: str):
    path = "C:\\Users\\geryj\Documents\\Index Copy\\"
    file_name = word + ".txt"
    with open(path + file_name, 'r') as f:
        res = f.readline().split(',')
    f.close()
    return res
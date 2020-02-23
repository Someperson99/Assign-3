# index builder
import re

class Posting:
    def __init__(self, docid, tfidf, fields=None):
        self.docid = docid
        self.tfidf = tfidf  # use freqcounts for now
        self.fields = fields

    def __repr__(self):
        return str.format("DOC ID: {} \nCOUNT : {} \nFIELDS: {}", self.docid, self.tfidf, self.fields)

"""
Simple in memory inverted index, based off of lectures
Does not have partial indexing yet
"""
def build_index(docs: dict()) -> dict():
    index = dict()
    doc_num = 0
    # TODO partial indexing, but don't need for milestone 1
        # while docs:
        #     batch = get_batch(docs)
    for (url, doc) in docs.items():
        doc_num = doc_num + 1
        tokens = parse(doc)
        for token in tokens:
            if token not in index:
                index[token] = [Posting(doc_num, 1)]
            else:
                # if the current doc id is the same, update freqcount (no need to create new Posting object)
                if (index[token][-1]).docid == doc_num:
                    (index[token][-1]).tfidf = (index[token][-1]).tfidf + 1
                else:
                    index[token].append(Posting(doc_num, 1))
    return index


"""
Parsing text str to get a list of tokens.
    Reused from part 2 Assignment 2 @miKeEt
"""
def parse(text: str) -> list():
    data = []
    newList = []
    data = re.split('[^a-z]+', text.lower())
    data = list(filter(None, data))
    for i in data:
        newList.append(i)
    return newList

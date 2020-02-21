# index builder

class Posting:
    def __init__(self, docid, tfidf, fields):
        self.docid = docid
        self.tfidf = tfidf  # use freqcounts for now
        self.fields = fields

    def __repr__(self):
        return str.format("DOC ID: {} \nCOUNT : {} \nFIELDS: {}", self.docid, self.tfidf, self.fields)


# TODO index construction procedure
def build_index(txt_docs: set()) -> dict():
    return dict()


if __name__ == "__main__":
    pass



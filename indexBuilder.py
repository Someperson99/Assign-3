# Index Builder
class Posting:
    def __init__(self, docid, tfidf, fields):
        self.docid = docid
        self.tfidf = tfidf  # use freqcounts for now
        self.fields = fields

    def __repr__(self):
        return str.format("DOC ID: {} \nCOUNT : {} \nFIELDS: {}\n", self.docid, self.docid, self.fields)

# TODO index construction procedure
def build_index(txt_docs: set()) -> dict():
    pass



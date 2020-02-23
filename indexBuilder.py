# index builder

class Posting:
    def __init__(self, docid, tfidf):
        self.docid = docid
        self.freq = tfidf  # use freqcounts for now
        

    """ def __repr__(self):
        return str.format("docId: {} \tfreq: {} \nFIELDS: {}", self.docid, self.freq) """
    def __repr__(self):
        return str.format("docId:: {} freq: {} \n", self.docid, self.freq)
    def get_ocId(self):
       return self.docid
    def get_freq(self):
       return self.docid
  
# TODO index construction procedure
def build_index(txt_docs: set()) -> dict():
    return dict()




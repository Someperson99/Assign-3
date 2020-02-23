# index builder

class Posting:
    def __init__(self, docid, tfidf):
        self.docid = docid
        self.freq = tfidf  # use freqcounts for now
        
    def __repr__(self):
        return str.format("docId:: {} freq: {} \n", self.docid, self.freq)
    def get_ocId(self):
       return self.docid
    def get_freq(self):
       return self.docid
  



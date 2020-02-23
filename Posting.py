class Posting:
    def __init__(self, docid, tfidf, fields=None):
        self.docid = docid
        self.tfidf = tfidf  # use freqcounts for now
        self.fields = fields

    def __repr__(self):
        return str.format("DOC ID: {} \nCOUNT : {} \nFIELDS: {} \n", self.docid, self.tfidf, self.fields)

    def get_docid(self):
        return self.docid

    def get_tfidf(self):
        return self.tfidf

    def get_fields(self):
        return self.fields

    # I dont want to reset value each time, i think incrementing would prevent overriding errors
    def increment_tfidf(self): # using freqcounts for now
        self.tfidf += 1

    # not sure yet how we want to implement fields, we can change this later
    def set_fields(self, new_field):
        self.fields.add(new_field)

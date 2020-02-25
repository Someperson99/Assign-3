class Posting:
    def __init__(self, docid, tfidf, fields=None):
        self.posting_tuple = (docid, tfidf, fields)
        self.docid = self.posting_tuple[0]
        self.tfidf = self.posting_tuple[1]  # use freqcounts for now
        self.fields = self.posting_tuple[2]

    def __repr__(self):
        return str.format("DOC ID: {} \nCOUNT : {} \nFIELDS: {} \n", self.docid, self.tfidf, self.fields)

    def __str__(self):
        if self.fields is None:
            return "(", + str(self.docid) + "," + str(self.tfidf) + ")"
        else:
            return "(", + str(self.docid) + "," + str(self.tfidf) + "," + str(self.fields) + ")"

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

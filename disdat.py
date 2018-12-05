from itertools import izip, imap

# You can choose not to cache data to memory if you like

class ColData:
    
    def __init__(self, vdfile, tdtfile, cache_all=True):
        self.vdfile  = vdfile
        self.tdtfile = tdtfile

        self.coldata   = None
        self.rowdata   = None
        self.n         = None
        self.valcounts = None

        if cache_all:
            self.cache_format()
            self.cache_coldata()
            self.cache_rowdata()

    def cache_coldata(self):
        self.coldata = map(list,self.vars())

    def cache_rowdata(self):
        self.rowdata = map(list,self.dats())

    def cache_format(self):
        self.valcounts = list(self.nof_vals())
        self.n = self.N()


    def nof_vals(self):
        if self.valcounts != None:
            return self.valcounts 
        else:
            return (l.count("\t") for l in file(self.vdfile))

    def vars(self):
        if self.coldata != None:
            return self.coldata
        else:
            return (imap(int, l.split()) for l in file(self.tdtfile))

    def dats(self):
        if self.rowdata != None:
            return self.rowdata
        else:
            return izip(*self.vars())

    def N(self):
        if self.n != None:
            return self.n
        else:
            n=-1
            for n,d in enumerate(self.dats()): pass
            return n+1

class RowData:
    
    def __init__(self, vdfile, datfile):
        self.vdfile  = vdfile
        self.datfile = datfile

    def nof_vals(self):
        for l in file(self.vdfile):
            yield l.count("\t")

    def vars(self):
        return izip(*self.dats())

    def dats(self):
        for l in file(self.datfile):
            yield imap(int, l.split())

    def N(self):
        for n,d in enumerate(self.dats()): pass
        return n+1

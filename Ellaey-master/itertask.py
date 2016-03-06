__author__ = 'Hash'

"""


||||||||||||||||||||||task general structure|||||||||||||||||||||

               a Task, in comparison to an Iterator
                   has a static amount of inputs

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



||||||||||||||||tasks and methods relations||||||||||||||||||||||


     There are two global variables in charge of relations
              one is a dict that makes a relation
                between task sequences and tasks
         the other makes one between methods and tasks


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



||||||||||||||||||||||inner task structure|||||||||||||||||||||||

                        function protocol

Each function in a task *must* receive the same list of inputs
        and return a different or equal list of outputs



|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


"""


def foo():
    print "yeah.. right"

def roo():
    print "like you'd succeed"
    return "you're awesome bro! "


_sf = [foo,roo]  # supported functions
_st = {0: [_sf[0], _sf[1]],
       1: [_sf[1]]}  # supported tasks
_s_t_s = {1: [_st[0], _st[1]]}  # supported task sequences


class Task:
    func = []
    output = []
    input = []
    id = 0

    def __init__(self, f, i):

        self.func = f
        self.input = i
        id += 1

    def activate(self):
        output = []
        for func in self.func:
            oi = func(self.input())
            if oi is not None:
                output.append(oi)
        self.output.append(output)

"""

i - input action(s)
o - output action(s)
sequance - which task sequance are we supporting in this iteration?
place - the current iterator
"""


class TaskIterator:

    def __init__(self, i, o, s):
        self.i = i
        self.o = o
        self.sequence = s
        self.place = 0

    def __iter__(self):
        return self

    def next(self, add_seq):
        if self.place < _s_t_s[self.sequence]:
            self.place += 1
            return Task(_s_t_s[self.sequence],self.o)
        else:
            if add_seq is None:
                return StopIteration
            else:
                self.sequence = add_seq[0]
                add_seq.remove[0]
                self.place = 0
            return Task(_s_t_s[self.sequence],self.o)

def add_functions(fs):
    if type(fs).isinstance(type([])):
        for f in fs:
            _sf.append(f)
    else:
        _sf.append(fs)


def find_functions(fs):
    index_func = []
    if type(fs).isinstance(type([])):
        for f in fs:
            if _sf.index(f) != -1:
                index_func.append(_sf)

    else:
        index_func.append(_sf.index(fs))
    return index_func


def add_tasks(ts):
    if type(ts).isinstance(type([])):
        for t in ts:  # t is a multi value, it contains a number of functions
            index_func = find_functions(t)
            ar_functions = []
            for i in index_func:
                ar_functions.append(_sf[i])
            _st.update({sorted(_st.keys())[-1] : ar_functions})

    else:
        index_func = find_functions(ts)
        ar_functions = []
        for i in index_func:
            ar_functions.append(_sf[i])
        _st.update({sorted(_st.keys())[-1] : ar_functions})


def find_tasks(ts):
    key_tasks = []
    if type(ts).isinstance(type([])):
        for t in ts:
            if _st[t]:
                key_tasks.append(t)

    else:
        key_tasks.append(_st[ts])
    return key_tasks


def add_seq(seqs):
    if type(seqs).isinstance(type([])):
        for seq in seqs:
            index_tasks = find_tasks(seq)
            ar_tasks=[]
            for i in index_tasks:
                ar_tasks.append(_st[i])
            _s_t_s.update({sorted(_s_t_s.keys())[-1] : ar_tasks})
    else:
        index_tasks = find_tasks(seqs)
        ar_tasks = []
        for i in index_tasks:
            ar_tasks.append(_st[i])
        _s_t_s.update({sorted(_s_t_s.keys())[-1] : ar_tasks})
"""
_sf = [foo,roo]  # supported functions
_st = {0: [_sf[0], _sf[1]],
       1: [_sf[1]]}  # supported tasks
_s_t_s = {1: [_st[0],_st[1]]}  # supported task sequences

"""
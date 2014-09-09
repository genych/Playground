import itertools

def init(func):
    def wrapper(*args):
        temp = func(*args)
        next(temp)
        print('Init done')
        return temp
    return wrapper

@init
def rec(n):
    for i in range(n):
        inp = yield
        print('Got:', inp)

def gen(string):
    pm = itertools.permutations(string, len(string)//2)
    yield from pm

r = rec(10)
g = gen('habr!')

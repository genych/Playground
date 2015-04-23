from concurrent.futures import ThreadPoolExecutor
import time
pool = ThreadPoolExecutor(2)

def lazy():
    for i in range(10):
        print(i)
        time.sleep(1)

def ask(some):
    i = input('what? ')
    print(i + ' yeah!', some.result())

lz = pool.submit(lazy)
lz.add_done_callback(ask)

import time
from functools import lru_cache

@lru_cache(maxsize = 10)

def some_work(n):
    time.sleep(3)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(5)
    # some_work(7)

    print("Done.... calling again")
    some_work(3)
    print("called again")

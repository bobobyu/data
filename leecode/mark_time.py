import time

def time_(func):
    def inner(*args, **kwargs):
        strat = time.clock()
        func(*args, **kwargs)
        print(time.clock()-strat)
    return inner

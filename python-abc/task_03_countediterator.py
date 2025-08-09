#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterator, counter=0):
        self.iterator = iter(iterator)
        self.counter = counter

    def __next__(self):
        vlaue = next(self.iterator)
        self.counter += 1
        return vlaue
        

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

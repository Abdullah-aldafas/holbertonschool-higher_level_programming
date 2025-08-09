#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterator, counter=0):
        self.__iterator = iter(iterator)
        self.__counter = counter

    def __next__(self):
        self.__counter += 1
        return next(self.iterator)

    def get_count(self):
        return self.__counter

    def __iter__(self):
        return self

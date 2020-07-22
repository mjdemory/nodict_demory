#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = '???'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value
        # Your code here
        return

    def __repr__(self):
        # Your code here
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        # Your code here
        if isinstance(self, other.__class__):
            return self.key == other.key
        else:
            return NotImplemented


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = None
        # Your code here

    def __repr__(self):
        # Your code here
        return

    def add(self, key, value):
        # Your code here
        return

    def get(self, key):
        # Your code here
        return

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return

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
        self.buckets = [ [] for _ in range(num_buckets) ]
        self.bucket_list = self.buckets
        # Your code here

    def __repr__(self):
        # Your code here
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        new_node = Node(key, value)
        bucket_index = hash(new_node) % self.buckets
        # Stuck here. Not sure if this is how to attain index of bucket.
        
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

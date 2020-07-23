#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = """Michael DeMory and helped by
                Tiffany McLean, Zac Gerber, JT, Peiro."""


class Node:
    def __init__(self, key, value=None):
        """Initilize data members of class when object is created"""
        self.hash = hash(key)
        self.key = key
        self.value = value
        # Your code here
        return

    def __repr__(self):
        """Makes the object readable"""
        # Your code here
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Compares object to other"""
        # Your code here
        if isinstance(self, other.__class__):
            return self.key == other.key
        else:
            return NotImplemented


class NoDict:
    def __init__(self, num_buckets=10):
        """Initilize data members of class when object is created"""
        self.buckets = [[] for _ in range(num_buckets)]
        # Your code here
        self.num = num_buckets

    def __repr__(self):
        """Makes the object readable"""
        # Your code here
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                         for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """Adds new object to bucket"""
        new_node = Node(key, value)

        bucket_index = self.buckets[new_node.hash % self.num]

        for i in bucket_index:
            if i == new_node:
                bucket_index.remove(i)
                break
        bucket_index.append(new_node)

        # Your code here

    def get(self, key):
        """Looks up key"""
        node_to_find = Node(key)

        bucket_index = self.buckets[node_to_find.hash % self.num]

        for i in bucket_index:
            if i == node_to_find:
                return i.value
        raise KeyError(f'{key} not found')

        # Your code here

    def __getitem__(self, key):
        """Uses get function"""
        # Your code here
        return self.get(key)

    def __setitem__(self, key, value):
        """Uses add function"""
        # Your code here
        return self.add(key, value)

"""
Goal: to create a MapSet object that can import json directly and wrap
    the object and allow for schemaless attribute access.

    2 parts: 
        1.  The Maap object which wraps json as a dict-like object
        2.  The MapSet that t
"""
import json
from collections import abc

# Factory methods
def load(data):
    pass

def loads(data):
    pass


class MapSet(abc.Mapping, abc.Set):

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


    # Mapping methods
    def __getitem__(self, key):
        pass

    def __missing__(self, key):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    
    # Set methods
    def __contains__(self, key):
        pass


    # Common methods
    def __iter__(self, key):
        pass

    def __len__(self, key):
        pass

    # Access methods
    def __getattr__(self, key):
        pass
"""
Goal: to create a MapSet object that can import json directly and wrap
    the object and allow for schemaless attribute access.

    2 parts: 
        1.  The Maap object which wraps json as a dict-like object
        2.  The MapSet that t
"""
import json
from collections import abc
from functools import reduce

# Factory methods
class Json:
    @staticmethod
    def load(path):
        with open(path, 'r') as f:
            data = f.read()

        if data:
            return MapSet(json.load(data))

    @staticmethod
    def loads(data):
        return MapSet(json.loads(data))


    class StrEncoder(json.JSONEncoder):
        def default(self, obj): #pylint: disable=method-hidden
            if getattr(obj,'__json__'):
                return obj.__json__()
            return obj

    @staticmethod
    def print(*data):
        for d in data:
            try:
                _d = json.dumps(d, indent=2, cls=Json.StrEncoder)
            except Exception as e:
                _d = d

            print(_d)
    
jprint = Json.print


class MapSet(abc.Mapping, abc.Set):
    """This is a docstring"""
    def __init__(self, *args):
        def _reduce(a,b):
            if not isinstance(b, (list)):
                b = [b]
            return [k for k in a+b if k]

        args = reduce(_reduce, args, [])

        self.__data__ = []
        for arg in args:
            if isinstance(arg, dict):
                self.__data__.append(arg)

        for d in self.__data__:
            for k,v in d.items():
                if isinstance(v,dict):
                    d[k] = MapSet(v)
                if isinstance(v,list):
                    if len(v) > 0:
                        if all(isinstance(e,dict) for e in v):
                            d[k] = MapSet(v)

    def __str__(self):
        return str(self.__data__)

    def __repr__(self):
        return '<MapSet Object>'
        
    def __json__(self):
        return self.__data__


    # Mapping methods
    def get(self, key, default=None):
        vals = []
        for d in self.__data__:
            vals.append(d.get(key, default))
        return vals

    def __getitem__(self, key):
        if isinstance(key, (int,slice)):
            return self.__data__[key]
        elif isinstance(key, str):
            print(key)

    def keys(self):
        keys = set()
        for d in self.__data__:
            for k in d.keys():
                keys.add(k)
        return keys

    def values(self):
        pass

    def items(self):
        pass

    
    # Set methods
    def __contains__(self, key):
        pass


    # Common methods
    def __iter__(self, key):
        for k in self.__data__:
            yield k

    def __len__(self):
        return len(self.__data__)

    # Access methods
    def __getattr__(self, key):
        pass



if __name__ == '__main__':
    with open('test_a.json', 'r') as f:
        data_a = json.load(f)

    with open('test_b.json', 'r') as f:
        data_b = json.load(f)

    with open('test_c.json', 'r') as f:
        data_c = json.load(f)

    ms = MapSet()
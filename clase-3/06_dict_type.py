"""
  Case-insensitive sections in ConfigParser
"""

from collections import OrderedDict
from collections.abc import MutableMapping
from configparser import ConfigParser

class CaseInsensitiveDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._d = OrderedDict(*args, **kwargs)
        self._convert_keys()
    def _convert_keys(self):
        for k in list(self._d.keys()):
            v = self._d.pop(k)
            self._d.__setitem__(k, v)
    def __len__(self):
        return len(self._d)
    def __iter__(self):
        return iter(self._d)
    def __setitem__(self, k, v):
        self._d[k.lower()] = v
    def __getitem__(self, k):
        return self._d[k.lower()]
    def __delitem__(self, k):
        del self._d[k.lower()]


parser = ConfigParser(dict_type=CaseInsensitiveDict)
# parser = ConfigParser()
parser.read('06_dict_type.ini')

print()
print()
print(parser.get('bug_tracker', 'url'))
print(parser.get('Bug_tracker', 'url'))
print(parser.get('Bug_Tracker', 'url'))
print()






import itertools
from configparser import ConfigParser

class MiDiccionario(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = itertools.count()

    def __setitem__(self, k, v):
        print("Key =" + k + ", value=", v)
        if k == "textsize":
            n = next(self.c)
            k = k + str(n)
        super().__setitem__(k, v)

print("----------------------------------------")
conf = ConfigParser(dict_type=MiDiccionario)
conf.read("07_dict_type.ini")
print("----------------------------------------")
print(conf["general"]["textsize0"])
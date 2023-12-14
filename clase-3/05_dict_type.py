import configparser

parser = configparser.ConfigParser()
parser.read_dict({'section1': {'key1': 'value1',
                               'key2': 'value2',
                               'key3': 'value3'},
                  'section2': {'keyA': 'valueA',
                               'keyB': 'valueB',
                               'keyC': 'valueC'},
                  'section3': {'foo': 'x',
                               'bar': 'y',
                               'baz': 'z'}
                  })

print()
print(parser.sections())
print()
for clave in parser.sections():
    for option in parser.options(clave):
        print(clave, option)
# print([option for option in parser['section2']])

parser.read("05_dict_type.ini")

print()
print(parser.sections())
print()
# print([option for option in parser['section2']])
for clave in parser.sections():
    for option in parser.options(clave):
        print(clave, option)

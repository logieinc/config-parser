import configparser

parser = configparser.ConfigParser()
# parser.read_dict({
#   "section": {
#     "keyA": "valueA",
#     "key": "valueB",
#     "keyC": "valueC"
#   },
#   "section1": {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
#   },
#   "section3": {
#     "ba": "y",
#     "baz": "z",
#     "foo": "x"
#   }
# })

#  parser.read_dict({'section1': {'key1': 'value1',
#                                'key2': 'value2',
#                                'key3': 'value3'},
#                   'section2': {'keyA': 'valueA',
#                                'keyB': 'valueB',
#                                'keyC': 'valueC'},
#                   'section3': {'foo': 'x',
#                                'bar': 'y',
#                                'baz': 'z'}
#                   })

parser.read_dict({
  "section": {
    "keyA": "valueA",
    "key": "valueB",
    "keyC": "valueC"
  },
  "section1": {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
  },
  "section3": {
    "ba": "y",
    "baz": "z",
    "foo": {
        "pepe": "pepe",
        "pepe2": "pepe2"
    }
  }
})

print()
print(parser.sections())
print()
for clave in parser.sections():
    for option in parser.options(clave):
        value = parser.get(clave, option)
        print(clave, option, value)

value = parser.get('section3', 'foo.pepe')

print(value)

# print([option for option in parser['section2']])

# parser.read("configjson.ini")
#
# print()
# print(parser.sections())
# print()
# # print([option for option in parser['section2']])
# for clave in parser.sections():
#     for option in parser.options(clave):
#         value = parser.get(clave, option)
#         print(clave, option, value)

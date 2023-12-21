import configparser

parser = configparser.ConfigParser()

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
    "foo": "x"
  }
})

print()
print(parser.sections())
print()
for clave in parser.sections():
    for option in parser.options(clave):
        value = parser.get(clave, option)
        print(clave, option, value)

# value = parser.get('section3', 'foo')
#
# print(value)

from configparser import ConfigParser

"""
converter = {'lista': lambda x: [i.strip() for i in x.split(',')],
                              'list': lambda x: [i.strip() for i in x.split(',')]
                              }
cp = ConfigParser(converters=converter)
"""

config = ConfigParser(converters={'lista': lambda x: [i.strip() for i in x.split(',')],
                              'list': lambda x: [i.strip() for i in x.split(',')]
                              })
config.read('converters_custom_types_listas.ini')


print('Converter lista:')
print(config.getlista('Germ', 'germs'))

print("")
print("Converter list:")
print(config['Germ'].getlist('germs'))

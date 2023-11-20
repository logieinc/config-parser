

import configparser


config = configparser.ConfigParser()
config.optionxform = lambda x: x.lower()

config.read("optionxform.ini")

for name in config.options('DATABASE'):
    string_value = config.get('DATABASE', name)
    print(f'  {name:<12} : {string_value!r:<7}')



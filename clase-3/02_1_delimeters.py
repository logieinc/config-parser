import configparser

config = configparser.ConfigParser(delimiters=('|', '='))

config.read('02_1_delimeters.ini')
config.get('GENERAL', 'Atributo1')
print(config)

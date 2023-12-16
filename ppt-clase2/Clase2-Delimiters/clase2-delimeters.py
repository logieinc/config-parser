import configparser

config = configparser.ConfigParser(delimiters=('|','='))

config.read('delimeters.ini')
config.get('GENERAL', 'Atributo1')
print(config)

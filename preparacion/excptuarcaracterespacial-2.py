import configparser

config = configparser.ConfigParser()

config['Seccion'] = {'Texto': 'Este es un valor con un caractér especial: $'}
config['Seccion']['Texto'] = configparser._UNSET

# config['Seccion'] = {'Texto': 'Este es un valor con un caractér especial: \\$'}

print(config['Seccion']['Texto'])

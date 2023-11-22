import configparser
"""
    Valores por defecto, en ausencia en archivo .ini toma dichos valores
"""

# Diccionario de valores predeterminados
defaults = {'key1': 'default_value_for_key1',
            'key2': 'default_value_for_key2'}

config = configparser.ConfigParser(defaults=defaults)

# Leer el archivo de configuración
config.read('00_defaults.ini')

key1_value = config.get('Section1', 'key1')
key2_value = config.get('Section1', 'key2')

# Imprimir los valores
print("")
print(f'key1: {key1_value}')
print(f'key2: {key2_value}')

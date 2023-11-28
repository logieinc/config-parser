"""

    Pruebas de los diferentes metodos del config parser

"""
import configparser
import os

config = configparser.ConfigParser()
config.read("pruebasconfig.ini")

print(config.get('Simple Values', 'key'))
print(config.get('Simple Values', 'spaces in keys'))
print(config.get('Simple Values', 'api key'))
print(config.get('Simple Values', 'key2', fallback='no hay key2'))
print(config.get('Simple Values', 'key'))
print(config.get('Simple Values', 'key'))

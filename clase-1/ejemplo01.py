"""

    Lectura archivo INI y exposicion de valores por consola

"""
import configparser

config = configparser.ConfigParser()
config.read("ejemplo01.ini", 'utf-8')

print(config["DEFAULT"]["ServerAliveInterval"])
print(config.get('DEFAULT', 'ServerAliveInterval'))

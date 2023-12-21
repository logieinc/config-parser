import configparser

config = configparser.ConfigParser()
config.read("ejemplo.ini")

print(config)
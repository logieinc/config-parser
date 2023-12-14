import configparser


config = configparser.ConfigParser(delimiters=['=', ':', '@', '>'])
# config = configparser.ConfigParser(delimiters=['=', ':', '@'])
config.read("02_delimiters.ini")

print()
print(config["DEFAULT"]["interval"])
print(config.get('DEFAULT', 'name'))
print(config.get('DEFAULT', 'zzz'))
print(config.get('DEFAULT', 'xxx'))
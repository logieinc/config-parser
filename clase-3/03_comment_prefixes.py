import configparser


config = configparser.ConfigParser(comment_prefixes=[';', '#', '%'])
config.read("03_comment_prefixes.ini")

print()
print(config["DEFAULT"]["interval"])
print(config.get('DEFAULT', 'name'))


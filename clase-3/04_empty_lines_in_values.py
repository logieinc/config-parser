import configparser


config = configparser.ConfigParser(empty_lines_in_values=True)
config.read("04_empty_lines_in_values.ini")

print()
print(config["Section"]["key"])
print(config["Section"]["key2"])
print()
print(config["Section02"]["data2"])



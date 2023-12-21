import configparser

import json

import datetime


def to_str(value):
    if type(value) == int:
        return str(value)
    elif type(value) == float:
        return str(value)
    elif type(value) == datetime.datetime:
        return value.strftime("%Y-%m-%dT%H:%M:%S")
    elif type(value) == list:
        value: str = ",".join(value)
        return value
    else:
        return value

with open('archivo5.json', 'r') as f:
    data = json.load(f)

print(data)

print(json.dumps(data, indent=4))

config = configparser.ConfigParser()

for section, options in data.items():
    config[section] = {}
    for option, value in options.items():
        value = to_str(value)
        config[section][option] = value


for section in config.sections():
    print(f"[{section}]")
    for option in config.options(section):
        value = config.get(section, option)
        print(f"{option} = {value} -> {type(value)}")
    print()  # Agregar una línea en blanco entre secciones

with open("archivojsonToIni.ini", "w") as f:
    config.write(f)


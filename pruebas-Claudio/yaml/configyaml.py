import configparser

import yaml

import datetime


def to_str(value):
    if type(value) == int:
        return str(value)
    elif type(value) == float:
        return str(value)
    elif type(value) == datetime.datetime:
        return value.strftime("%Y-%m-%dT%H:%M:%S")
    else:
        return value

def print_config(config):
    # Imprimir todas las secciones y opciones
    print()
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option)
            print(f"{option} = {value} -> {type(value)}")
        print()  # Agregar una línea en blanco entre secciones

class YamlConfigParser(configparser.ConfigParser):

    def read_yaml(self, filename):
        with open(filename) as f1:
            data = yaml.safe_load(f1)

            for section, options in data.items():
                self.add_section(section)
                for option, value in options.items():
                    value = to_str(value)
                    self.set(section, option, value)


parser = YamlConfigParser()
parser.read_yaml('config.yaml')

with open("config.ini", "w") as f:
    parser.write(f)

print_config(parser)
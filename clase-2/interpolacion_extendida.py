"""
    Interpolacion Extendida (ExtendedInterpolation)

"""
import configparser
import os


def print_config(config):
    # Imprimir todas las secciones y opciones
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option, vars=os.environ)
            print(f"{option} = {value}")
        print()  # Agregar una línea en blanco entre secciones

if __name__ == "__main__":

    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    # config = configparser.ConfigParser()
    config.read("interpolacion_extendida.ini")

    print_config(config)



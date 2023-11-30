"""

    Interpolacion básica

"""
import configparser

def print_config(config):
    # Imprimir todas las secciones y opciones
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option)
            print(f"{option} = {value}")
        print()  # Agregar una línea en blanco entre secciones

if __name__ == "__main__":

    #config = configparser.ConfigParser(interpolation=configparser.BasicInterpolation())
    config = configparser.ConfigParser()
    config.interpolation = configparser.BasicInterpolation()
    config.read("interpolacion_basica.ini")

    print_config(config)


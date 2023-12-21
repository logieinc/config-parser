# Impresion setores

import configparser


def print_config(config):
    # Imprimir todas las secciones y opciones
    print()
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option)
            print(f"{option} = {value} -> {type(value)}")
        print()  # Agregar una línea en blanco entre secciones


configiso = configparser.ConfigParser()

configiso.read("00_configiso.ini")

print_config(configiso)
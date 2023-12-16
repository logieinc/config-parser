"""
Añade una nueva sección llamada “NuevaSeccion” al archivo de configuración predeterminado.
Agrega al menos tres configuraciones dentro de esta nueva sección.
Modifica el código para leer y mostrar las configuraciones de esta nueva sección.
"""

import configparser

# Crear un objeto ConfigParser

config = configparser.ConfigParser()

# Ruta del archivo de configuración predeterminado

default_config_path = 'ejemplo02.ini'

# Leer el archivo de configuración predeterminado

with open(default_config_path, 'r', encoding='cp1250') as default_config_file:
    config.read_file(default_config_file)

# Añadir una nueva sección llamada NuevaSeccion

nueva_seccion = 'NuevaSeccion'
config.add_section(nueva_seccion)

# Agregar al menos tres configuraciones dentro de la nueva sección

config.set(nueva_seccion, 'opcion1', 'valor1')
config.set(nueva_seccion, 'opcion2', 'valor2')
config.set(nueva_seccion, 'opcion3', 'valor3')

# Imprimir configuraciones actualizadas

for section in config.sections():
    print(f"[{section}]")
    for option, value in config.items(section):
        print(f"{option} = {value}")

with open('ejemplo02.ini', 'w') as f:
    config.write(f)

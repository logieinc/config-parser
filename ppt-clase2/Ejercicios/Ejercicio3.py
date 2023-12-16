"""
Pide al usuario que ingrese su nombre de usuario.
Utiliza este nombre de usuario para crear una nueva ruta de archivo de configuración específica del usuario, por ejemplo, ~/{nombre_de_usuario}_config.cfg.
Pregunta al usuario por tres opciones diferentes: texto, numero, y boolean
Modifica el código para leer este nuevo archivo de configuración del usuario si existe.
Imprime en la consola todas las secciones y configuraciones leídas."""

import configparser
import os

# Crear un objeto ConfigParser

config = configparser.ConfigParser()

# Preguntar al usuario por su nombre de usuario

nombre_usuario = input("Ingresa tu nombre de usuario: ")

# Utilizar el nombre de usuario para crear la ruta del archivo de configuración del usuario

ruta_usuario = os.path.expanduser(f'~/PruebasPython/{nombre_usuario}_config.cfg')

# Leer el nuevo archivo de configuración del usuario si existe

if os.path.exists(ruta_usuario):
    config.read([ruta_usuario], encoding='utf-8')
    print(f"Configuración del usuario {nombre_usuario}:")

# Preguntar al usuario por tres opciones diferentes, incluyendo cadena multilinea y opción bandera

configuracion_usuario = {}
configuracion_usuario['opcion_texto'] = input("Ingresa una cadena de texto: ")
configuracion_usuario['opcion_numerica'] = input("Ingresa un número: ")
configuracion_usuario['opcion_bandera'] = input("Ingresa True o False para una opción bandera: ")

# Agregar las configuraciones del usuario a la sección 'ConfiguracionUsuario'

config.add_section('ConfiguracionUsuario')

for opcion, valor in configuracion_usuario.items():
    config.set('ConfiguracionUsuario', opcion, valor)

# Imprimir todas las secciones y configuraciones leídas

for section in config.sections():
    print(f"[{section}]")
    for option, value in config.items(section):
        print(f"{option} = {value}")

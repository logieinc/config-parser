"""Ejercicio 1:

Exploración de Configuraciones Predeterminadas

Crea un archivo de configuración predeterminado llamado defaults.cfg
con al menos tres secciones y cinco configuraciones en total.

Imprime en la consola todas las secciones y configuraciones leídas."""

import configparser

# Crear un objeto ConfigParser

config = configparser.ConfigParser()

# Crea las secciones

config.add_section('section1')
config.add_section('section2')
config.add_section('section3')

config.set('section1', 'atributo1', 'valor1')
config.set('section1', 'atributo2', 'valor2')
config.set('section2', 'atributo3', 'valor3')
config.set('section2', 'atributo4', 'valor4')
config.set('section3', 'atributo5', 'valor5')
config.set('section3', 'atributo6', 'valor6')

# Ruta del nuevo archivo de configuración predeterminado

default_config_path = 'defaults.cfg'

# Escribe el nuevo archivo de configuración predeterminado

with open(default_config_path, "w", encoding='utf-8') as f:
        config.write(f)

# Imprimir todas las secciones y configuraciones leídas

for section in config.sections():
    print(f"[{section}]")
    for option, value in config.items(section):
        print(f"{option} = {value}")

"""

    Detecta si seccion DATABASE contiene clave 'user'
    Salida standard output secciones


"""
import configparser

config = configparser.ConfigParser()
config.read("ejemplo03.ini")

# Impresion setores
print(config.sections())

# Determina existencia de clave user
if 'user' in config['DATABASE']:
    print("Existe clave user")
else:
    print("No existe clave user")

# Claves en sector DATABASE
for clave in config['DATABASE']:
    print(clave)




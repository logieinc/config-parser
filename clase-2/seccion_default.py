# Leer el archivo de configuración

import configparser
configuracion = configparser.ConfigParser()
configuracion.read('seccion_default.ini')

# Añadir sección DEFAULT

configuracion['DEFAULT']['dificultad'] = 'alta'
configuracion['DEFAULT']['jugadores'] = '2'
configuracion['DEFAULT']['sonido'] = 'True'

print("------------ Seccion DEFAULT ---------------")
# Mostrar opciones y sus valores de DEFAULT
for opcion, valor in configuracion['DEFAULT'].items():
    print (opcion, ":", valor)

print("------------ Seccion General ---------------")
# Mostrar opciones y sus valores de General
for opcion in configuracion.items('General'):
    print (opcion)






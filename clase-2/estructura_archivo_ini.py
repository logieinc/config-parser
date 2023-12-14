"""
    Estructura soportada archivos ini

    Personalizando el comportamiento del parser

"""
import configparser

config = configparser.ConfigParser(allow_no_value = True)

#config = configparser.ConfigParser()
config.read("estructura_archivo_ini.ini")

print(config.get('Multiline Values', 'chorus'))
print('\n\n\n',config.get('Sections Can Be Indented', 'multiline_values'))
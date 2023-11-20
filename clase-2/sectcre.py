#
# Personalizando el comportamiento del parser
#
# Configuracion SECTCRE
#
#   Expresion regular online = https://regex101.com
#
#


import configparser
import re

config = """
            [Section 1]
            option = value
            [  Section 2  ]
            another = val
        """

typical = configparser.ConfigParser()
typical.read_string(config)

print("------------ SECTCRE default ---------------")
print(typical.sections())
custom = configparser.ConfigParser()
print("")

print("------------ SECTCRE re-configurado ---------------")
custom.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
custom.read_string(config)
print(custom.sections())



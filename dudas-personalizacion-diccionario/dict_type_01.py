from configparser import ConfigParser, ExtendedInterpolation

# Define un diccionario personalizado para almacenar las opciones de configuración
class MyDict(dict):
    def __setitem__(self, key, value):
        # Puedes personalizar la forma en que se almacenan las opciones
        super(MyDict, self).__setitem__(key, value.upper())

# Crea un objeto ConfigParser y especifica el tipo de diccionario personalizado
config = ConfigParser(interpolation=ExtendedInterpolation(), dict_type=MyDict)

# Agrega algunas opciones de configuración
config['Section1'] = {'option1': 'value1', 'option2': 'value2'}
config['Section2'] = {'option3': 'value3', 'option4': 'value4'}

# Imprime las opciones de configuración almacenadas en el diccionario personalizado
for section in config.sections():
    print(f"[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")
from configparser import ConfigParser

class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(key.lower())

# Crear un objeto ConfigParser y especificar el tipo de dict personalizado
config = ConfigParser(dict_type=CaseInsensitiveDict)

# Para que cancele
# config = ConfigParser(interpolation=None)

# Agregar opciones de configuración con claves insensibles a mayúsculas y minúsculas
config['Section1'] = {'Option1': 'Value1', 'Option2': 'Value2'}
config['Section2'] = {'Option3': 'Value3', 'Option4': 'Value4'}

# Acceder a las opciones de configuración con claves insensibles a mayúsculas y minúsculas
print(config['section1']['option1'])  # Salida: Value1
print(config['SECTION2']['OPtION3'])  # Salida: Value3

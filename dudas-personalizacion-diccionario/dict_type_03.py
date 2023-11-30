"""

  Personalizacion de diccionario configparser

    En este caso se desea obtener el dato primitivo clase de los valores detectados por expresiones regulares

    Validate ISO 8601 Dates and Times
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch04s07.html

    Expresion regular ISO
    https://www.debuggex.com/r/_G6Mvw1eoYJF2Bgf

"""
import datetime
from configparser import ConfigParser
import re

class MiDicionario(dict):

    # Pattern date time
    patternISO8601 = re.compile(
            r'^(?P<full>((?P<year>\d{4})([/-]?(?P<mon>(0[1-9])|(1[012]))([/-]?(?P<mday>(0[1-9])|([12]\d)|(3[01])))?)?(?:T(?P<hour>([01][0-9])|(?:2[0123]))(\:?(?P<min>[0-5][0-9])(\:?(?P<sec>[0-5][0-9]([\,\.]\d{1,10})?))?)?(?:Z|([\-+](?:([01][0-9])|(?:2[0123]))(\:?(?:[0-5][0-9]))?))?)?))$')

    # Pattern first last name
    patternFirstLastName = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)")
    def __setitem__(self, key, value):
        super(MiDicionario, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        valor = super(MiDicionario, self).__getitem__(key.lower())
        if not isinstance(valor, str):
            return valor
        if self.patternISO8601.match(valor):
            return datetime.datetime.strptime(valor, '%Y-%m-%dT%H:%M:%S.%f')
        if self.patternFirstLastName.match(valor):
            firstName = self.patternFirstLastName.match(valor)["first_name"]
            lastName = self.patternFirstLastName.match(valor)["last_name"]
            return firstName
        return valor

    def __contains__(self, key):
        return super(MiDicionario, self).__contains__(key.lower())


def print_config(config):
    # Imprimir todas las secciones y opciones
    print()
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option)
            print(f"{option} = {value} -> {type(value)}")
        print()  # Agregar una línea en blanco entre secciones

parser = ConfigParser(interpolation=None, dict_type=MiDicionario)
parser.read('dict_type_03.ini')

print_config(parser)







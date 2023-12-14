import configparser
from string import Template

config = configparser.ConfigParser()

config.read('template.ini')

template = Template(config.get('MAIL', 'template'))

lista_mail = (('El gran Hot Dog', 'Claudio Romano', 'Somos una empresa especialistas en perros calientes'),
              ('La Pizza Rabieta', 'Fabian Giordano', 'Pizzas como ninguna'),
              ('Empanadas las Tucu Tucu', 'Fabiana Rivarola', 'Hechas como en casa'))

for i in lista_mail:
    print(template.substitute(nombre_empresa=i[0], nombre_usuario=i[1], informacion_empresa=i[2]))

# empresa = 'El gran Hot Dog'
# usuario = 'Claudio Romano'
# informacion = 'Somos una empresa especialistas en perros calientes'

# mail = template.substitute(nombre_empresa=empresa, nombre_usuario=usuario, informacion_empresa=informacion)

# print(mail)
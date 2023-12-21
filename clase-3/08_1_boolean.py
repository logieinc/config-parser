import configparser

config = configparser.ConfigParser()

config.read("08_1_boolean.ini")

entorno = config.get('opciones avanzadas', 'entorno')
mostrar_logs = config.getboolean('opciones avanzadas', 'mostrar logs')

if mostrar_logs:
    print(f'  {entorno:<12}', mostrar_logs)
else:
    print('sin log')

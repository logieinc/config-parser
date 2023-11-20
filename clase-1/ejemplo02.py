"""

    Escritura de archivo INI

"""
import configparser

config = configparser.ConfigParser()

config['DATABASE'] =  {  'hostname' : 'localhost', 'name' : 'database' }

config.add_section('SERVER')
config.set('SERVER', 'ip', '127.0.0.1')
config.set('SERVER', 'port', '80')


with open("ejemplo02.ini", "w") as f:
    config.write(f)


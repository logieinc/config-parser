import configparser
import os

config = configparser.ConfigParser()

# Rutas de archivo de configuración

default_config_path = 'default.cfg'
site_config_path = 'site.cfg'
user_config_path = os.path.expanduser('~/PycharmProjects/config-parser/ppt/Clase2-slide28/myapp.cfg')

with open(default_config_path, 'r', encoding='cp1250') as default_config_file:
    config.read_file(default_config_file)

# Leer otros archivos de configuración
config.read([site_config_path, user_config_path], encoding='cp1250')
# config.read([user_config_path, site_config_path], encoding='cp1250')
# config.read(site_config_path, encoding='cp1250')
# config.read(user_config_path, encoding='cp1250')

for name in config.options('PATH'):
    string_value = config.get('PATH', name)
    print(f'  {name:<12} : {string_value!r:<7}')

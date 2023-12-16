# Crear objeto ConfigParser

from configparser import ConfigParser
config = ConfigParser()

#import configparser
#config = configparser.ConfigParser()

# Leer archivo de configuración
config.read("config.ini")

# Acceder a configuraciones

username = config.get("General", "username")
password = config.get("General", "password")

print(username)
print(password)

# Verificar la existencia de configuraciones

if config.has_section("General"):
    print("Configuraciones generales encontradas")
    print(f"Usuario: {username}")
    print(f"Contraseña: {password}")
else:
    print("No se encontraron configuraciones generales")

# Lectura de configuraciones Unicode
nombre = config.get("Unicode", "nombre")
ciudad = config.get("Unicode", "ciudad")

print(f"Nombre:  {nombre} , Ciudad: {ciudad}")

# Acceso a configuraciones
database_host = config.get("Database", "host")
database_port = config.get("Database", "port")

print(f"host de la base de datos: {database_host} , Puerto: {database_port} ")

# Lectura de configuraciones convertir de unicode a ISO

# Crear objeto ConfigParser
configiso = ConfigParser()

# Leer archivo de configuración en ISO
configiso.read("configiso.ini", encoding="ISO-8859-1")
nombreiso = configiso.get("ISO-8859-1", "nombre")
ciudadiso = configiso.get("ISO-8859-1", "ciudad")

print(f"Nombre:  {nombre} , Ciudad: {ciudad}")
print(f"Traducido de utf8 a iso Nombre  {nombreiso} , Ciudad: {ciudadiso}")

#config.read("configiso.ini", encoding="ISO-8859-1")
#nombreiso = config.get("ISO-8859-1", "nombre")
#ciudadiso = config.get("ISO-8859-1", "ciudad")

#print(f"Nombre  {nombre} , Ciudad: {ciudad}")
#print(f"Traducido de utf8 a iso Nombre  {nombreiso} , Ciudad: {ciudadiso}")

#config.read("config.ini", encoding="ISO-8859-1")
#nombreiso = config.get("Unicode", "nombre")
#ciudadiso = config.get("Unicode", "ciudad")

#print(f"Nombre  {nombre} , Ciudad: {ciudad}")
#print(f"Traducido de utf8 a iso Nombre  {nombreiso} , Ciudad: {ciudadiso}")
import configparser


def get_code_from_ini(archivo):
    """Obtiene el código para ejecutar de un archivo .ini."""

    config = configparser.ConfigParser()
    config.read(archivo)

    codigo = config["code"]["code"]
    return codigo


def execute_code(codigo):
    """Ejecuta el código proporcionado."""

    exec(codigo)


filename = "09_code.ini"
code = get_code_from_ini(filename)
execute_code(code)

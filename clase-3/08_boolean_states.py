import configparser

config = configparser.ConfigParser()
config.BOOLEAN_STATES = {
    "yes": True,
    "true": True,
    "on": True,
    "no": False,
    "false": False,
    "off": False,
    "enabled": True,
    "prendido": True,
    "apagado": False
}

config.read("08_boolean_states.ini")
for name in config.options('boolean perzonalizado'):
    string_value = config.get('boolean perzonalizado', name)
    value = config.getboolean('boolean perzonalizado', name)
    print('  {:<12} : {!r:<7} -> {}'.format(
        name, string_value, value))
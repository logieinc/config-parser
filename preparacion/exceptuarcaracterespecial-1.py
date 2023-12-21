import configparser

# Crear objeto ConfigParser
config = configparser.ConfigParser()

# Agregar sección y configuraciones
config.add_section('Seccion')
config.set('Seccion', 'Opcion1', 'Valor1 $')
config.set('Seccion', 'Opcion2', 'Valor2 %%')

# Imprimir configuración utilizando la API heredada
for option, value in config.items('Seccion'):
    print(f"{option} = {value}")

# Crear objeto RawConfigParser para exceptuar caracter especial

raw_config = configparser.RawConfigParser()
raw_config.set(None, 'Opcion3', 'Valor3 %')

# raw_config['Seccion]['Opcion4'] = 'Valor4'
# print(f"Opcion3 = {raw_config['Opcion3']}")
# for option, value in raw_config.items('Seccion'):
#     print(f"{option} = {value}")

for section in raw_config.sections():
    print(f"[{section}]")
    for option in raw_config.options(section):
        value = raw_config.get(section, option)
        print(f"{option} = {value} -> {type(value)}")
    print()  # Agregar una línea en blanco entre secciones

# print(raw_config.get(None, 'Opcion3'))

"""
    Valores requeridos

"""
import configparser

conf = configparser.ConfigParser()
conf.read("01_requerido.ini")
conf.set("required", ["username", "password"])

print(conf["general"]["username"])
print(conf["general"]["password"])
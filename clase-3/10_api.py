"""
    Interpolacion Extendida ejemplo API (ExtendedInterpolation)

    Debemos configurar archivo ini para realzar llamadas a API.

    Tenemos como base url el siguiente valor: https://jsonplaceholder.typicode.com, en sector
    denominado [API]

    Por otro lado tenemos el sector [ENDPOINTS] con dos valores claves
        posts = base_url + /posts
        comments = base_url + /comments

    Crear archivo ini basado en interpoación extendida e imprimir por consola los valores de posts y comments.

"""
import configparser
import json

import requests

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read("10_api.ni")

# Call API
posts = config.get('ENDPOINTS', 'posts')
comments = config.get('ENDPOINTS', 'comments')

print(posts)
print(comments)

headers = {}
response = requests.get(posts, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Imprimir el objeto JSON formateado
    print(json.dumps(data, indent=4))
else:
    print(f"Error en la llamada a la API: {response.status_code}")

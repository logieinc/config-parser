from configparser import ConfigParser
import datetime


def parse_iso_datetime(s):
    print('parse_iso_datetime({!r})'.format(s))
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f')



config = ConfigParser(converters={'lista': lambda x: [i.strip() for i in x.split(',')],
                                  'list': lambda x: [i.strip() for i in x.split(',')],
                                  'datetime': parse_iso_datetime,
                                  })

config.read('11_converters_custom_lista_date.ini')

print('Converter lista:')
print(config.sections())
print(config.getlista('Germ', 'germs'))
print(config.get('Germ', 'germs'))

print("")
print("Converter list:")
# print(config['Germ'].getlist('germs'))
print(config['Germ'].get('germs'))

string_value = config['datetimes']['due_date']
value = config.getdatetime('datetimes', 'due_date')
print('due_date : {!r} -> {!r}'.format(string_value, value))

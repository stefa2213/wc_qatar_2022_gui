import json


def save_object(object_, filename):
    with open(filename, 'w') as file:
        json.dump(object_, file)


def read_object(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# if __name__ == '__main__':
#     dictionar = {'a': 18, 'b': True, 'c': 1.5}
#     save_object(dictionar, 'mag.json')
#     dictionar_citit = read_object('mag.json')
#     print(dictionar_citit)

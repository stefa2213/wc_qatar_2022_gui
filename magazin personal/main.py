import json_library
from clase import Produs
from pprint import pprint

# produse = []
# json_library.save_object(produse, 'mag.json')
file = 'mag.json'
produse = json_library.read_object(file)

def interpret_command(command):
    if command == "1":
        produs = add_products()
        produse.append(produs)
        json_library.save_object(produse, 'mag.json')
    elif command == "2":
        show_products(produse)


def afisare_meniu():
    print("0. Iesire...")
    print("1. Adaugare produs...")
    print("2. Afisare...")


def add_products():
    name = input("name: ")
    price = input("price: ")
    category = input("category: ")
    quantity = input("quantity: ")
    description = input("description: ")
    return Produs(name, float(price), category, int(quantity), description)

def show_products(produse):
    pprint(produse)


afisare_meniu()
command = input("Introduceti o comanda: ")

while command != '0':
    interpret_command(command)
    afisare_meniu()
    command = input("Introduceti o comanda: ")

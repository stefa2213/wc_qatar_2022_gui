from pprint import pprint
import pickle_library
import os
from clasa_produs import Produs, Categorie

# produse = []
# pickle_library.save_object_to_filename(produse, "produse.pickle")
fisier = "produse.pickle"
# fisier_categ = fisier[3]
produse = pickle_library.read_object_from_filename(fisier)
categorie = pickle_library.read_object_from_filename(fisier)


def interpret_command(command):
    if command == "1":
        produs = adaugare_produse()
        produse.append(produs)
        pickle_library.save_object_to_filename(produse, "produse.pickle")
    elif command == "2":
        afisare_produse(produse)
    elif command == "3":
        stergere_produs(produse)
    elif command == "4":
        modificare_produs(produse)
    elif command == "5":
        vanzare_produs(produse)
    elif command == "6":
        pass
    elif command == "7":
        categ = adaugare_categorie()
        categorie.append(categ)
        pickle_library.save_object_to_filename(categorie, "produse.pickle")
    elif command == "8":
        afisare_categorie(categorie)
    elif command == "9":
        modificare_categorie(categorie)


def afisare_meniu():
    print("0. Iesire...")
    print("1. Adaugare produs...")
    print("2. Afisare...")
    print("3. Stergere...")
    print("4. Modificare...")
    print("5. Vanzare...")
    print("6. Testare...")
    print("7. Adaugare categorie...")
    print("8. Afisare categorie...")
    print("9. Modificare categorie...")


def adaugare_categorie():
    nume = input("nume categorie: ")
    return Categorie(nume)


def stergere_categorie():
    nume = input("nume categorie: ")
    categorie.remove(categorie)
    pickle_library.save_object_to_filename(categorie, "produse.pickle")


def afisare_categorie(categorie):
    pprint(categorie)


def modificare_categorie(categorie: list):
    alege_produs(categorie)
    modificare_proprietate_categorie(categorie)
    pickle_library.save_object_to_filename(categorie, "produse.pickle")


def modificare_proprietate_categorie(categorie):
    nume = input(f"nume (Enter pentru a lasa {categorie}): ")
    if nume != "":
        categorie.update(name=nume)


def adaugare_produse():
    nume = input("nume: ")
    cantitate = input("cantitate: ")
    descriere = input("descriere: ")
    pret = input("pret: ")
    categorie = input("categorie: ")
    return Produs(nume, float(pret), categorie, int(cantitate), descriere)
    # return {"nume": nume, "cantitate": int(cantitate), "descriere": descriere, "pret": float(pret),
    #         "categorie": categorie}


def afisare_produse(produse):
    pprint(produse)


def alege_produs(produse):
    for index, produs in enumerate(produse):
        print(index, produs)
    index_produs = int(input("Introduceti indexul: "))
    return produse[index_produs]


def stergere_produs(produse: list):
    produs = alege_produs(produse)
    produse.remove(produs)
    pickle_library.save_object_to_filename(produse, "produse.pickle")


def modificare_produs(produse: list):
    produs = alege_produs(produse)
    modificare_proprietate_produs(produs)
    pickle_library.save_object_to_filename(produse, "produse.pickle")


def modificare_proprietate_produs(produs):
    nume = input(f"nume (Enter pentru a lasa {produs.name}): ")
    cantitate = input(f"cantiate (Enter pentru a lasa {produs.cantitate}): ")
    descriere = input(f"descriere (Enter pentru a lasa {produs.descriere}): ")
    pret = input(f"pret (Enter pentru a lasa {produs.pret}): ")
    categorie = input(f"categorie (Enter pentru a lasa {produs.categorie}): ")
    if nume != "":
        produs.update(name=nume)
    if cantitate != "":
        produs.update(cantitate=int(cantitate))
    if descriere != "":
        produs.update(descriere=descriere)
    if pret != "":
        produs.update(pret=float(pret))
    if categorie != "":
        produs.update(categorie=categorie)


def modificare_camp_produs(produs, *campuri):
    for camp in campuri:
        valoare_noua = input(f"{camp}(Enter pentru a lasa {produs[camp]}): ")
        if valoare_noua != "":
            if camp == "cantitate":
                produs[camp] = int(valoare_noua)
            elif camp == "pret":
                produs[camp] = float(valoare_noua)
            else:
                produs[camp] = valoare_noua
    return produs


def vanzare_produs(produse: list):
    produs: Produs = alege_produs(produse)
    cantitate_produs = int(input(f"Introdu cantitatea (Max) {produs.cantitate}: "))
    produs.update(cantitate=produs.cantitate - cantitate_produs)
    # produs.cantitate = produs.cantitate - cantitate_produs
    pickle_library.save_object_to_filename(produse, "produse.pickle")


afisare_meniu()
command = input("Introduceti o comanda: ")

while command != '0':
    interpret_command(command)
    afisare_meniu()
    command = input("Introduceti o comanda: ")

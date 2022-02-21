# Sa se scrie o clasa Categorie, cu nume, produse. Sa se integreze in magazin cu creare, stergere, modificare

class Categorie:
    def __init__(self, nume, produse):
        self.nume = nume
        self.produse = produse

        def __str__(self):
            return f"{self.nume} {self.produse}"

        def __repr__(self):
            return str(self)

        def update(self, name=None):
            if name is not None:
                self.name = name


class Produs:
    def __init__(self, name="", pret=0, categorie="", cantitate=0, descriere=""):
        self.name = name  # set the default value for the name field of the Animal class object
        self.cantitate = cantitate
        self.descriere = descriere
        self.pret = pret
        self.categorie = categorie

    def __str__(self):
        return f"{self.name} {self.cantitate} {self.pret} {self.categorie}"

    def __repr__(self):
        return str(self)

    def update(self, name=None, pret=None, categorie=None, cantitate=None, descriere=None):
        if name is not None:
            self.name = name
        if pret is not None:
            self.pret = pret
        if categorie is not None:
            self.categorie = categorie
        if cantitate is not None:
            self.cantitate = cantitate
        if descriere is not None:
            self.descriere = descriere


if __name__ == '__main__':
    sapca = Produs(name="Sapca Nike", pret=15, categorie="Barbati", cantitate=5, descriere="Alba")
    # sapca.update(name = "ceapica")
    print(sapca)
#
# def print_details(self):  # method for printing the state of an object
#     print(f"Name: {self.name}, age: {self.cantitate}.")

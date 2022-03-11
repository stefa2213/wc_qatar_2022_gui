class Produs:
    def __init__(self, name="", price=0, category="", quantity=0, descripion=""):
        self.name = name
        self.price = price
        self.category = category
        self.price = price
        self.description = descripion

    def __str__(self):
        return f"{self.name} {self.cantitate} {self.pret} {self.categorie}"

    def __repr__(self):
        return str(self)
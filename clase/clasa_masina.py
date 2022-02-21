class Vehicul:
    def __init__(self, culoare, nr_roti, motorizare, nr_locuri):
        self.culoare = culoare
        self.nr_roti = nr_roti
        self.motorizare = motorizare
        self.nr_locuri = nr_locuri

    def __str__(self):
        return f'{self.culoare} {self.nr_roti}'


class Masina(Vehicul):
    def __init__(self, brand, model, capacitate_cilindrica, putere, culoare, motorizare, nr_locuri):
        super().__init__(culoare, 4, motorizare, nr_locuri)
        self.brand = brand
        self.model = model
        self.capacitate_cilindrica = capacitate_cilindrica
        self.putere = putere

    def __str__(self):
        return f'{self.brand} {self.model}'


vehicul = Vehicul('albastru', 7, 'diesel', '5')
masina = Masina('Volvo', 'XC90', '1.4T tdi', '120 cai', 'negru', 'diesel', 5)
print(masina, '-', vehicul)


class Locatar:
    def __init__(self, nume, prenume, data_nasterii):
        self.nume = nume
        self.prenume = prenume
        self.data_nasterii = data_nasterii

    def __repr__(self):
        return f'{self.nume} {self.prenume} {self.data_nasterii}'


class Apartament:
    def __init__(self, numar, suprafata, locatari):
        self.numar = numar
        self.suprafata = suprafata
        self.locatari = locatari


locatar1 = Locatar('Stefan', 'Nosca', '1991-11-14')
locatar2 = Locatar('Stefan', 'Stefan', '1991-10-14')
apartament = Apartament(23, '11mp', [locatar1, locatar2])
print(locatar1.nume, locatar1.prenume, locatar1.data_nasterii)
print(apartament.numar, apartament.suprafata, apartament.locatari)

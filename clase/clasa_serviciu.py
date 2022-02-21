# Sa se scrie clasa Serviciu, cu proprietatile nume, durata, pret

class Serviciu:
    def __init__(self, nume, durata, pret):
        self.nume = nume
        self.durata = durata
        self.pret = pret

    def __str__(self):
        return f'{self.nume} {self.durata} {self.pret}'

    def __repr__(self):
        return f'{self.nume} {self.durata} {self.pret}'


class Spalare(Serviciu):
    def __init__(self, nume, durata, pret, cantaite_sampon, cantitate_apa):
        super().__init__(nume, durata, pret)
        self.cantitate_sampon = cantaite_sampon
        self.cantitate_apa = cantitate_apa
    def __str__(self):
        return f'{self.nume} {self.durata} {self.pret} {self.cantitate_sampon} {self.cantitate_apa}'


# Sa se scrie o clasa Frizer, cu proprietatile nume, prenume, servicii

class Frizer:
    def __init__(self, nume, prenume, servicii):
        self.nume = nume
        self.prenume = prenume
        self.servicii = servicii

    def __str__(self):
        return f'{self.nume} {self.prenume}'

#Sa se scrie clasa Programare cu nume, prenume, data, ora, serviciu, frizer

class Programare:
    def __init__(self, nume, prenume, data, ora, serviciu, frizer):
        self.nume = nume
        self.prenume = prenume
        self.data = data
        self.ora = ora
        self.serviciu = serviciu
        self.frizer = frizer
    def __str__(self):
        return f'{self.nume} {self.prenume} {self.data} {self.ora} pentru {self.serviciu} {self.frizer}'


serviciu = Serviciu('tuns', '0.5h', '25')
serviciu_spalare = Spalare('Spalare par scurt', '10min', '15lei', '30ml', '4l')
frizer = Frizer('Costache', 'Gigi', [serviciu])
programare = Programare('barsan', 'Marius', '1990-10-12', '14:00:02.01', serviciu, frizer)
print(programare)
print(frizer)
print(serviciu_spalare)

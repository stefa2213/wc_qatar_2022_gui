# Tema: 21.feb

# 0. Fiind data o lista cu numere, sa se scrie o functie care returneaza o lista cu radicalii de ordin 3 al elementelor din lista de intrare.

print('rezolvare ex.0')

def rad_3(list):
    result = []
    for n in list:
        result.append(n ** (1/3))
    return result

ls = [27, 8, 64, 125]
print(rad_3(ls))

# 1. Sa se scrie o functie pentru rezolvarea ecuatiei de grad 2. Parametri de intrare: a, b, c. parametri de iesire: x1, x2.

def ecuatie_gr2(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - d ** (1 / 2)) / (2 * a)
        x2 = (-b + d ** (1 / 2)) / (2 * a)
        print('raspuns ex.2: Solutia are doua radacini reale: x1:', x1, 'si x2:', x2)
    elif d == 0:
        x = -b / (2 * a)
        print('raspuns ex.2: Solutia are o singura radacina reala:', x)
    else:
        print('raspuns ex.2: Solutia nu are radacini reale')


ecuatie_gr2(2, 10, 12)
#
# # 2. Fiind dat un pret de 25.72 lei cu tot cu TVA, sa se calculeze pretul fara TVA (tva = 19% din pret)
#
print('rezolvare ex.2')

pret_intreg = 25.72
pret_fara_TVA = pret_intreg - (pret_intreg * 0.19)

print(f'{pret_fara_TVA: .2f}')
#
#
# # 3. Fiind data o lista de dictionare de forma
# # cos = [{'pret':19.5, 'cantitate': 3}, ...]
# # a) Sa se calculeze valoarea totala a cosului.
#
def cos_cumparaturi(cos:list):
    sume_cos = []
    for index, elem in enumerate(cos):
        suma_produs = cosul[index]['pret'] * cosul[index]['cantitate'] + cosul[index]['adaos']
        sume_cos.append(suma_produs)
    return sume_cos

cosul = [{'produs': 'branza', 'pret': 6.5, 'cantitate': 2, 'adaos': 0}, {'produs': 'prosop', 'pret': 3.5, 'cantitate': 5, 'adaos': 0},
       {'produs': 'apa', 'pret': 1.5, 'cantitate': 4, 'adaos': 0}]

valoare_totala_cos = sum(cos_cumparaturi(cosul))
print('Valoarea totala a cosului este:', valoare_totala_cos)
#
# # b) Sa se aplice o reducere de 15% pe tot cosul.
#
print('Valoarea totala a cosului cu o reducere de 15% este:', valoare_totala_cos * 0.85)
#
# # 4. Fiinda dat un adaos de 40% pe oricare din produsele din cosul de mai sus, sa se calculeze profitul facut pe cosul respectiv
#
adaos = float(input('Introduceti adaosul produsului in procente: '))
adaos_branza = cosul[0]['pret'] * adaos/100
print(adaos_branza, 'Este profitul facut pe cosul nostru')
#
#
# # 5. Sa se scrie o clasa Cetatean cu nume, prenume, cnp.
# # print('rezolvare ex.5')
#
class Cetatean:
    def __init__(self, nume, prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp

class Locatar:
    def __init__(self, nume, prenume, apartament, varsta):
        self.nume = nume
        self.prenume = prenume
        self.apartament = apartament
        self.varsta = varsta
#
# # 6. Fiind date clasele Cetatean si Locatar, sa se scrie o noua clasa Rezident care sa mosteneasca din ambele.
#
# print('rezolvare ex.6')

class Rezident:
    def __init__(self, nume, prenume, cnp, apartament, varsta):
        Locatar.__init__(self, nume, prenume, varsta, apartament)
        Cetatean.__init__(self, nume, prenume, cnp)

    def __str__(self):
        return f'{self.nume} {self.prenume} {self.cnp} {self.apartament} {self.varsta}'

locuitor = Rezident('Georgel', 'Popescu', '1911114095562', '32', '25')

print(locuitor)
#
# # 7. Sa se scrie o functie care primeste ca parametru o lista cu numere,  si returneaza o tupla cu 2 liste formate din patratele, respectiv cuburile perfecte din lista initiala.
#
#
print('rezolvare ex.7"')

def patr_cub(list):
    lista_patrate = []
    lista_cuburi = []
    for n in list:
        lista_patrate.append(n ** 2)
        lista_cuburi.append(n ** 3)
    return (lista_patrate, lista_cuburi)

lista_numere = [2,3,4,5,6]

print(patr_cub(lista_numere))





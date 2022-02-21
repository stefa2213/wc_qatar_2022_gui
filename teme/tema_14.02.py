print('tema 14.02')
# 1. Sa se afiseze tabla inmultirii de la 1 pana la 10
# 1 2 3 4 5 6 7 8 910
# 2 4
# 3 6
# 4
# 5
# 6
# 7
# 8
# 9
# 10
print('rezolvare ex.1')

tabla_ = int(input('Introdu numarul pentru care vrei sa se afiseze tabla inmultirii:'))
nr = 1
for nr in range(1, 10 + 1):
    result = tabla_ * nr
    print(tabla_, '*', nr, '=', result)
    nr += 1


print('\n')
print('rezolvare ex.2')

# 2. a) Sa se afiseze pe ecran echivalentul unui chenar pentru imageinea cu bradul (piramida), ca mai jos:

# [[***                   ***],
# [**                     **],
# [*                       *],
#
#            ...
#
# *                       *
# **                     **
# ***                   ***
# ]

def list_de_liste_rama(i):
    prov = i
    lista = []
    for i in range(prov, -1, -1):
        lista.append(f"{'*' * i}{' ' * (20 + (prov - i) * 2)}{'*' * i}")

    lista.append(f"{' ' * ((20 + prov * 2) // 2 - 2)}{'.' * 4}{' ' * ((20 + prov * 2) // 2 - 2)}")

    for i in range(0, prov + 1, 1):
        lista.append(f"{'*' * i}{' ' * (20 + (prov - i) * 2)}{'*' * i}")
    return lista

def afisare_lista(lista):
    for row in lista:
        print(row)

lista = list_de_liste_rama(5)
afisare_lista(lista)


# 2. b) Sa se scrie o functie care intoarce o lista de liste care contine caracterele pentru afisat, si o alta functie care face afisarea efectiva.
# 2. c) Sa se refactorizeze (modifice) functia care genereaza imaginea, sa primeasca ca parametru numarul de stele pe orizontala/verticala dintr-un colt al chenarului.
# 2. d) Sa se scrie o functie care genereaza lista de liste cu bradul+cerul (vezi pe Slack, pe #exercitii), si poate fi apelata impreuna cu functia de afisare.
# 3. e) Sa se scrie o functie care genereaza bradul cu cer, si cu rama de 4 stele.

# 4. Sa se calculeze suma tuturor numerelor impare intre 0 si 100.

print('rezolvare ex.4')

suma = []
x = 0

for x in range(0, 100):
    if x % 2 == 1:
        suma.append(x)
    else:
        continue
    x += 1
print(suma)
print(sum(suma))


# 5. Sa se scrie o functie care calculeaza media armonica a oricator numere.

print('rezolvare ex.5')

# from statistics import harmonic_mean

def harmonic_mean(args):
    # n / (1/x1 + 1/x2 + 1/x3 ... + 1/xn)
    n = len(args)
    suma_tuturor_elementelor = 0
    for numar in args:
        suma_tuturor_elementelor += 1/numar
    return n / suma_tuturor_elementelor

lst = []
x = input('Introdu numarul:')


while x.isnumeric():
    lst.append(int(x))
    x = input('Introdu numarul: / alt caracter pentru iesire..')

media_h = harmonic_mean(lst)
print(media_h, 'este media armonica a numerelor tale')



# 6. Sa se scrie o functie care calculeaza factorialul unui numar dat ca parametru de intrare (n! = 1*2*3*4*...*n).

print('rezolvare ex.6')

# import math
#
# x = int(input('Introdu numarul pentru care vrei sa se calculeze factorialul:'))
# def fact(x):
#     factorial = math.factorial(x)
#     return factorial
#
# rezultat = (fact(x))
# print('Rezultatul factorialului pentru numarul', x, 'este', rezultat)


# 7. Sa se scrie o functie care primeste ca parametru de intrare un string de forma "123,45 Lei", si intoarce valoarea float a numarului din string. Hint: atentie la caracterele invalide, si la despartitorul zecimal.

def rem_lett(text = '123,45 Lei'):
    text = list(text)
    result = list()
    for letter in text:
        if letter not in 'Lei':
            result.append(letter)
    return ''.join(result)


suma_lei = '123,45 Lei'
suma_lei = suma_lei.replace(',', '.')
print(rem_lett(suma_lei))
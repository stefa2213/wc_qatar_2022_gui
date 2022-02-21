# 2. Sa se scrie o functie care primeste o lista de numere, si intoarce o lista cu cuburile numerelor impare din lista initiala (fiecare numar ridicat la puterea 3)

# print('rezolvare ex.2')
#
# lista = [11,2,5,4]
# cuburi = [i ** 3 for i in lista]
# print(cuburi)


# 3. Sa se scrie o functie care primeste ca parametru un numar float cu oricate zecimale, si il intoarce cu doar 2 zecimale, in format string
# print('rezolvare ex.3')
#
# def doua_zecimale(float):
#     print(f'{float: .2f}')
#     return float
#
# doua_zecimale(4.5667)

# a = 23.52655546
# print(f'{a: .2f}')

# 4. a)  Fiind date posibilitatile ╲ │ ╱ ─ , scrieti o functie care sa
# primeasca un parametru string de forma
# "╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─", si care sa returneze un string cu
# fiecare caracter intors 45' la dreapta.

# print('╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─')
#
# def rotate_bars(image):
#     for char in image:
#         if char == '╲':
#             image = image.replace(char, '│')
#         if char == '│':
#             image = image.replace(char, '╱')
#     return image
#         # image.replace('│', '╱')
#         # image.replace('/', '-')
#         # image.replace('-', '╲')
#         # image.replace('╲', '│')
#
# print(rotate_bars('╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─'))



# 4. b)  Fiind date cele de mai sus, faceti ca fiecare caracter sa se
# roteasca 45' * pozitia in string


def rotate_character(character, times=0):
    character_to_replace = "╲│╱─"
    replaced_characters = "╲│╱─"
    while times > 0:
        replaced_characters = replaced_characters[1:] + replaced_characters[0]
        times -= 1
    new_characters = character.maketrans(character_to_replace, replaced_characters)
    character = character.translate(new_characters)
    return character


def rotate_characters(characters):
    result = ""
    for index, character in enumerate(characters):
        new_character = rotate_character(character, times=index)
        result += new_character
    return result


test = "╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─"
parameter = rotate_characters(test)
print(parameter)


# 5. Sa se scrie o functie care primeste o lista de elemente si un numar
# de elemente pentru combinari, si genereaza combinarile acestora.
# (Hint: combinarile efective, nu numarul lor)

print('rezolvare pentru exercitiul 5')

import math

#varianta 1

# def lista_fact(nlist, k):
#     kf = math.factorial(k)
#     return [math.factorial(n) / (kf * math.factorial(n - k)) for n in nlist]

#varianta 2

def lista_fact(list, k):
    result = []
    for n in list:
        result.append(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
    return result

lista = []
n = input('Introdu valoarea lui n: ')

while n.isnumeric():
    lista.append(int(n))
    n = input('Introdu numarul: / alt caracter pentru iesire..')

k = int(input(('Introduceti valoare lui k: ')))

print('Combinarile efective ale numerelor tale "n" sunt:', lista_fact(lista, k))



# 6. Sa se scrie o functie care afiseaza un cerc in consola cu caractere ░.
# (v2: atentie la inaltimea si latimea caracterului in terminal)



# 7. Scrieti o functie care primeste un cod IBAN de Romania prin parametru si il valideaza (intoarce True daca e valid, False daca nu).
# https://en.wikipedia.org/wiki/International_Bank_Account_Number


# Romania   RO09 BCYP 0000 0012 3456 7890 - varianta coleg Ciprian

alphabet = {chr(i + 65): i + 10 for i in range(0, 26)}
print(dict)


def check_iban(iban):
    len_check = iban.replace(" ", "")
    if len(len_check) != 24:
        print("Contul IBAN nu are lungimea corespunzatoare. IBAN-ul este invalid")
        return False

    # moved_characters_1 = len_check[1:] + len_check[0]
    # # The code [1:0] prints from the second character till the last + [0] add the first character.
    # moved_characters_2 = moved_characters_1[1:] + moved_characters_1[0]
    # moved_characters_3 = moved_characters_2[1:] + moved_characters_2[0]
    # moved_characters_4 = moved_characters_3[1:] + moved_characters_3[0]

    len_check = len_check[4:] + len_check[:4]

    # print(moved_characters_4)

    result = ""
    for character in len_check:
        if character in alphabet:
            result += str(alphabet[character])
        else:
            result += character
    # return result
    # print(result)

    if int(result) % 97 == 1:
        print("Contul IBAN valid")
        return True
    else:
        print("Contul IBAN este invalid")
        return False


if __name__ == '__main__':
    iban_check = check_iban("RO09 BCYP 0000 0012 3456 7890")
    print(iban_check)
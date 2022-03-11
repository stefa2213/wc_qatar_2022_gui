# 2. Sa se scrie o functie care genereaza toate combinatiile posibile a-z 0-9 de cate 3 caractere.
# pt 3:
# 'aaa', 'aab', 'aac', ..., 'aaz', 'aa0', 'aa1', ..., 'aa9',
# 'aba', 'abb', 'abc', ..., 'abz', 'ab0', 'ab1', ..., 'ab9',
# ...
# '99a', '99b', '99c', ..., '
# ...
# 3. Sa se dinamizeze functia de mai sus pentru orice numar de caractere. - rezolvat 'Alexandru'

import time
from pprint import pprint


def comb_alt(lista, length=4, initial=None, result=None):
    if result is None:
        result = []
    if initial is None:
        initial = []
    if len(initial) == length:
        str_value = ""
        for c in initial:
            str_value += c
        result.append(str_value)
        return result

    for item in lista:
        initial.append(item)
        index = len(initial) - 1
        result = comb_alt(lista, initial=initial, result=result)
        initial.pop(index)
    return result


def comb(list_):
    final_list = []
    for item in list_:
        first = item
        for item in list_:
            second = item
            for item in list_:
                third = item
                final_list.append(first + second + third)
    return final_list


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

t1 = time.time()
lala = comb_alt(list)
t2 = time.time()

print(lala)
print('Timpul necesar pentru gasirea celor', len(lala), 'de variante, a fost:', t2 - t1, 'secunde')

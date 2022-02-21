# class Animal:
#     def __init__(self, name = 'Rex', age = 3):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'<{self.name} {self.age}>'
#
# print(Animal())
#
# count = 0
# for letter in 'pip list -o (search for installed packages with a newer version to download)':
#     if letter == 'a':
#         count += 1
#
# print("There are", count, "letters of \'A\'")
#
#
# for i in range(2, 16, 3):
#     print(i)

# n = 2.526455
# print(f'{n: .3f}')
#
# per = 0.5546
# print(f'{per: .1%}')

# import os
#
# for folder in range(0, 11):
#     os.makedirs(str(folder))
# for folder in range(0, 6):
#     for subfolder in ['mon', 'tue', 'wed']:
#         os.makedirs(str(folder) + '/' + str(subfolder))

# my_list = [1,2,3,4,5,6,3,54,6,4,5,6,7,4,4,5,6,7,7,8,6,5,4]
# every_two = my_list[::2]
# print(every_two)
# print(sum(every_two) / len(every_two))


# x = 0
#
# while x < 5:
#     x += 1
#     if x == 4:
#         break
#     if x == 1:
#         continue
#     print(x)

# toate numerele pare intre 0  si 20

# x = 0
# while x <= 20:
#     x += 1
#     if x % 2 == 0:
#         print(f'{x} este par')


# # Sirul lui Fibbonaci
# a = 0
# b = 1
#
# while b <= 100:
#     c = a + b
#     a = b
#     b = c
#     print(b)

# # Fiind date 2 string-uri, stergeti din al doilea string toate literele care se regasesc in primul. din a toate literele care se regasesc in b
#
# a = ''' The Fibonacci numbers
#  were first described in Indian mathematics,[
#  2][3][4] as early as
#   200 BC in work by Pingala on enumerating possible
#    patterns of Sanskrit poetry formed from syllables
#    of two lengths. They are named after the Italian mat
#    hematician Leonardo of Pisa, later known as Fibona
#    cci, who introduced the sequence to Western Europea
#    n mathematics in his 1202 book Liber Abaci.[5]
# '''
# b = 'ci,'
#
# index = 0
#
# # while index < len(b):
# #     character = b[index]
# #     a = a.replace(character.upper(), '')
# #     a = a.replace(character, '')
# #     index += 1
# #
# # print(a)
#
# for car in b:
#     a = a.replace(car.upper(), '')
#     a = a.replace(car, '')
# print(a)


# username = input(str('Enter your age:'))
#
# print(f'numele userului este: {username}')
# print(type(username))


# import sys
#
# print(sys.argv)
#
# # de scris in 'terminal'
# # python sys_.py 23 45 65 56 56


# sa se genereze primele 20 de numere prime

# numar = 2
# count = 0
# list_nr_prime = []
#
# while count < 1000:
#     prim = True
#     for divizor in range(2, int(numar**1/2)):
#         if numar % divizor == 0:
#             prim = False
#             # print('numarul nu este prim')
#     if prim:
#         count += 1
#         list_nr_prime.append(numar)
#     numar += 1
# print(list_nr_prime)
# print(len(list_nr_prime))


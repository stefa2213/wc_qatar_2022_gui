# print('\n')
# print('ex.1')
# # 1. Avand o lista cu doctorate (care contine mai multe string-uri, fiecare string e un doctorat), scrieti un algoritm care sa verifice daca un alt string se afla in lista existanta. Daca da, sa se afiseze "plagiat", altfel "original".
#
# doctorat = ''' NOTE:	1. În practică va fi necesară o suprapuner
# 2. Încercaţi să adaptaţi această metodă propriului vostru stil.
# 3. Dacă v-a fost de folos încercaţi s-o transmiteţi şi altora.
# '''
#
# for elem in doctorat:
#     if 'propriului vostru caz' in doctorat:
#         print(f'Doctoratul este plagiat')
#     else:
#         print(f'Doctoratul este original')
# is comparing with every character instead of word..
#

# 2.Dintr-o lista cu numere, sa se afiseze 3 liste formate din numerele divizibile cu 2, 3, 5, ignorand restul numerelor.

lista_mea = [23, 45, 68, 25, 30, 60, 45, 90]
divizor2 = []
divizor3 = []
divizor5 = []
a = 0

while a < 50:
    a += 1
    if a % 2 == 0:
        divizor2.append(a)
    if a % 3 == 0:
        divizor3.append(a)
    if a % 5 == 0:
        divizor5.append(a)
        
print(divizor2)
print(divizor3)
print(divizor5)
# #
# #
# print('\n')
#
# # 3. printati toate patratele perfecte intre 0 si 1000 (incl 0, 1000)
#
# a = 0
# lst = []
# # while a in range(0, 1001):    #sa alegem una din cele doua
# while a <= 1000:                #sa alegem una din cele doua
#     c = a*a
#     if c > 1000:
#         break
#     lst.append(c)
#     a += 1
#
#     # print(c, 'este patrat perfect')
# print(f'numerele {lst} sunt patrate perfecte')
# #
# print('\n')
#
# # # Afisati toti divizorii unui numar.
# #
# a = 64
# x = 0
# lst = []
# for x in range(1, a + 1):
#     if a % x == 0:
#         # print(x, 'este divizorul lui', a)
#         lst.append(x)
#         x += 1
#     else:
#         continue
# print(f'{lst} sunt divizorii lui a')

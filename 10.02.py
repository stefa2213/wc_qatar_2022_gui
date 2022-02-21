# Sa se scrie o functie care primeste un CNP si il valideaza (calculeaza si verifica cifra de control).

# cnp = "2970215018111"
# cnp_control = "279146358279"
# suma = 0
# for index in range(12):
#     cifra_cnp = cnp[index]
#     cifra_control = cnp_control[index]
#     suma = suma + int(cifra_cnp) * int(cifra_control)
# print(suma)
#
# rest = suma % 11
# if rest == 10:
#     control = 1
# else:
#     control = rest
#
# print(control)
# print(cnp[-1] == str(control))
#
#
#
# def verificare_cnp(cnp):
#     cheie = '279146358279'
#     suma = 0
#     for index in range(12):
#         cifra_cnp = cnp[index]
#         cifra_control = cheie[index]
#         suma = suma + int(cifra_cnp) * int(cifra_control)
#
#     print(suma)
#     rest = suma % 11
#     if rest == 10:
#         control = 1
#     else:
#         control = rest
#
#     #print(control)
#     return (print(int(cnp[-1]) == control))
#
# cnp=input("introduceti CNP: ")
# #cnp = '2970215018111'
# verificare_cnp(cnp)


# def draw_pyramid(width):
#     print("." * width)
#     print("." * ((width - 1) // 2) + " " + "." * ((width - 1) // 2))
#     for index in range(1, width + 1, 2):
#         if index == width:
#             space = ""
#         else:
#             space = " "
#         print(f'{"." * ((width - index) // 2 - 1)}{space}{"*" * index}{space}{"." * ((width - index) // 2 - 1)}')
#
#
# draw_pyramid(23)


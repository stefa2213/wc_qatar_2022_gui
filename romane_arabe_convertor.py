# Se da un numar in caractere romane, sa se converteasca in cifre arabe.

dic_nr = {'M': 1000, 'C': 100, 'D': 500, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def convert_roman_number(numar_roman):
    numar_roman = numar_roman.upper()
    sum_ = 0
    for numeral in numar_roman:
        sum_ += dic_nr[numeral]
    sum_ = convert_sum(numar_roman, sum_)
    return sum_


def convert_sum(numar_roman, sum_):
    if 'IV' in numar_roman:
        sum_ = sum_ - 2
    if 'IX' in numar_roman:
        sum_ = sum_ - 2
    if 'XL' in numar_roman:
        sum_ = sum_ - 20
    if 'XC' in numar_roman:
        sum_ = sum_ - 20
    if 'CD' in numar_roman:
        sum_ = sum_ - 200
    if 'CM' in numar_roman:
        sum_ = sum_ - 200
    return sum_


numar_roman = input('Scrieti numarul in cifre romane: ')

print(convert_roman_number(numar_roman))

# numeral1 = numar_roman[0]
# if len(numar_roman) >= 2:
#     numeral2 = numar_roman[1]
# if len(numar_roman) >= 3:
#     numeral3 = numar_roman[2]
# if len(numar_roman) >= 4:
#     numeral4 = numar_roman[3]
# if len(numar_roman) >= 5:
#     numeral5 = numar_roman[4]
# if len(numar_roman) >= 6:
#     numeral6 = numar_roman[5]
# if len(numar_roman) >= 7:
#     numeral7 = numar_roman[6]
# if len(numar_roman) >= 8:
#     numeral8 = numar_roman[7]
# if len(numar_roman) >= 9:
#     numeral9 = numar_roman[8]


# for numeral in numar_roman[:]:
#     if len(numar_roman) == 1:
#         sum = dic_nr[numeral1]
#     if len(numar_roman) == 2:
#         sum = dic_nr[numeral1] + dic_nr[numeral2]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 3:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 4:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 5:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 6:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
#             numeral6]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 7:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
#             numeral6] + dic_nr[numeral7]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 8:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
#             numeral6] + dic_nr[numeral7] + dic_nr[numeral8]
#         sum = convert_sum(numar_roman, sum)
#     if len(numar_roman) == 9:
#         sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
#             numeral6] + dic_nr[numeral7] + dic_nr[numeral8] + dic_nr[numeral9]
#         sum = convert_sum(numar_roman, sum)

# print('Numarul a fost convertit in cifre arabe:', sum_)

# Note: The largest number you can write in Roman numerals is 3,999 which is MMMCMXCIX.
# You can represent numbers larger than 3,999 in Roman numerals using an overline.
# MMMCMXCIX == 3999

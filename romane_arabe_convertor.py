# Se da un numar in caractere romane, sa se converteasca in cifre arabe.

dic_nr = {'M': 1000, 'C': 100, 'D':500, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

def convert_roman_number(numar_roman):
    sum_ =  0


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
numar_roman = numar_roman.upper()


numeral1 = numar_roman[0]
if len(numar_roman) >= 2:
    numeral2 = numar_roman[1]
if len(numar_roman) >= 3:
    numeral3 = numar_roman[2]
if len(numar_roman) >= 4:
    numeral4 = numar_roman[3]
if len(numar_roman) >= 5:
    numeral5 = numar_roman[4]
if len(numar_roman) >= 6:
    numeral6 = numar_roman[5]
if len(numar_roman) >= 7:
    numeral7 = numar_roman[6]
if len(numar_roman) >= 8:
    numeral8 = numar_roman[7]
if len(numar_roman) >= 9:
    numeral9 = numar_roman[8]


for numeral in numar_roman[:]:
    if len(numar_roman) == 1:
        sum = dic_nr[numeral1]
    if len(numar_roman) == 2:
        sum = dic_nr[numeral1] + dic_nr[numeral2]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 3:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 4:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 5:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 6:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
            numeral6]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 7:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
            numeral6] + dic_nr[numeral7]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 8:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
            numeral6] + dic_nr[numeral7] + dic_nr[numeral8]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200
    if len(numar_roman) == 9:
        sum = dic_nr[numeral1] + dic_nr[numeral2] + dic_nr[numeral3] + dic_nr[numeral4] + dic_nr[numeral5] + dic_nr[
            numeral6] + dic_nr[numeral7] + dic_nr[numeral8] + dic_nr[numeral9]
        if 'IV' in numar_roman:
            sum = sum - 2
        if 'IX' in numar_roman:
            sum = sum - 2
        if 'XL' in numar_roman:
            sum = sum - 20
        if 'XC' in numar_roman:
            sum = sum - 20
        if 'CD' in numar_roman:
            sum = sum - 200
        if 'CM' in numar_roman:
            sum = sum - 200

print('Numarul a fost convertit in cifre arabe:', sum)

#Note: The largest number you can write in Roman numerals is 3,999 which is MMMCMXCIX.
# You can represent numbers larger than 3,999 in Roman numerals using an overline.
# MMMCMXCIX == 3999
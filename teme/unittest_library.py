# test 1

def f_to_m(feet):
    result = feet / 3.28048
    result = str(f'{result: .3f}')
    return result


def m_to_f(meters):
    result = meters * 0.3048
    result = str(f'{result: .3f}')
    return result

# test 2

def rem_lett(text):
    text = list(text)
    result = list()
    for letter in text:
        if letter not in 'Lei':
            result.append(letter)
    return ''.join(result)

# test 3

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
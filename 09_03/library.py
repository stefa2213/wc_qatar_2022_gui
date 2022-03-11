def celsius_to_fahrenheit(celsius):
    result = celsius * 9 / 5 + 32
    return result


def fahrenheit_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5 / 9
    return result

print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(32))


# if __name__ == '__main__':
#     print(fahrenheit_to_celsius(15))
#     print(f'library name {__name__}')



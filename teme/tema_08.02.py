catalog = {
    'elev1': 9,
    'elev2': 7,
    'elev3': 6,
    'elev6': 10,
    'elev4': 5,
    'elev5': 10
}
# comparam
lista_note = catalog.values()
final = max(lista_note)
for key in catalog:
    if catalog[key] == 10:
        print(key, 'a luat nota', final)


numar = 11233211

numar_txt = str(numar)
numar_txt_intors = numar_txt[::-1]

if numar_txt == numar_txt_intors:
    print(numar, 'e numar polindrom..')
else:
    print(numar, 'nu este numar polindrom..')


list1 = [2, 3, 4, 6, 7, 67, 45, 34, 65, 76, 32]
list2 = [3, 4, 5, 7, 3, 34, 5, 65, 76, 34, 23]
list3 = []

for element in list1:
    for elem in list2:
        x = (element, elem)
        list3.append(x)
print(list3)




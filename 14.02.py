# # Fraza = "O #Propoziție ^Este O Succesiune ()De Cuvinte Dintr-o Limbă /Oarecare"
#
# diacritice = {
#     " ": "-",
#     "ă": "a",
#     "â": "a",
#     "î": "i",
#     "ş": "s",
#     "ț": "t"
# }

# special_characters = "#^&*()+[]{};',./<>?"
#
#
# # caractere_de_inlocuit = " ăâîşţ"
# # caractere_inlocuitoare = "-aaist"
#
#
# def turn_to_url(text):
#     text = text.lower()
#     result = ''
#     for new_character in text:
#         if new_character in diacritice:
#             result += diacritice[new_character]
#         elif new_character in special_characters:
#             pass
#         else:
#             result += new_character
#     print(result)
#     return result
#
#
# turn_to_url('ăO #Propoziție ^Este O Succesiune ()De Cuvinte Dintr-o Limbă /Oarecare')




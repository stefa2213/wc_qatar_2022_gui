print('tema 09.02')
# Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele ...

def foo(text):
    for letter in text:
        text = text.replace('E', '3')
        text = text.replace('e', '3')
        text = text.replace('I', '1')
        text = text.replace('i', '1')
        text = text.replace('O', '0')
        text = text.replace('o', '0')
        text = text.replace('A', '4')
        text = text.replace('a', '4')
        text = text.replace('S', '5')
        text = text.replace('s', '5')
        text = text.replace('T', '7')
        text = text.replace('t', '7')
        return text


print(foo('''
The distress alert shall be sent through a satellite either
with absolute priority in general communication channels,
on exclusive distress and safety frequencies reserved for
satellite EPIRBs in the Earth-to-space direction
'''))








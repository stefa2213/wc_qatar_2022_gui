# tema 03.feb

# 1. sa se verifice daca un numar este divizibil cu 77

x = 152
if x % 77 == 0:
    print('solutia ex.1: numarul este divizibil cu 77')
else:
    print('solutia ex.1: numarul nu este divizibil cu 77')

# 2.fiind date 3 numere sa se verifice daca sunt numere pitagoreice

a = 3
b = 4
c = 5

if a**2 + b**2 == c**2:
    print('solutia ex.2: cele 3 numere sunt pitagoreice')
else:
    print('solutia ex.2: cele 3 numere nu sunt pitagoreice')

# 3.sa se calculeze volumul trunchiului de con cu inaltimea h si razezle de cerc R,r

# inaltimea = h
h = 7
R = 8
r = 3
pi = 3.14
# volum_trunci_con = V
V = pi*h * (R**2 + r**2 + R*r) / 3
print(f'solutia ex.3: volumul trunchiului de con este: {V: .1f}' )

# 4. sa se calculeze cmmdc a doua numere

a = 32
b = 12

if a > b:
    while a > b:
        a -= b
        while a < b:
            b -= a
            if a == b:
                print('solutia ex.4: CMMDC al celor 2 numere este:',a)
        if a == b:
            print('solutia ex.4: CMMDC al celor 2 numere este:',a)
elif a < b:
    while a < b:
        b -= a
        while a > b:
            a -= b
            if a == b:
                print('solutia ex.4: CMMDC al celor 2 numere este:',a)
        if a == b:
            print('solutia ex.4: CMMDC al celor 2 numere este:',a)
else:
    print('solutia ex.4: CMMDC al celor 2 numere este:',a)


# 5. sa se calculeze cmmmc a doua numere

a = 32
b = 12

init_a = a
init_b = b

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print('solutia ex.4: CMMDC al numerelor', init_a, 'si', init_b, 'este', a)

CMMMC = (init_b * init_a) // a
print('solutia ex.5: CMMMC al nuemerelor', init_a, 'si', init_b, 'este:', CMMMC)


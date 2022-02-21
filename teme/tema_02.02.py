# tema_02.feb

# 1.sa se scrie un algoritm care face media armonica a 3 numere: a,b,c
# media armonica = n / (1/n1 + 1 / n2 + 1 / n3 + ... + 1 / an)
# media_armonica = x

a = 2
b = 3
c = 4
x = 3 / ((1/a) + (1/b) + (1/c))

print('raspuns ex.1:', x)

# 2.sa se scrie un algoritm care rezolva ecuatia de gradul 2 (a*x1**2 + b*x2 + c = 0). se afla x1 si x2
# a*x1**2 + b*x2 + c = 0 > 2*x1**2 + 3*x2 = -4 >

a = 1
b = 5
c = 6
d = b**2 - 4*a * c

if d > 0:
    x1 = (-b - d**(1/2)) / (2*a)  #d**(1/2) = sqrt(d)
    x2 = (-b + d**(1/2)) / (2*a)
    print('raspuns ex.2: Solutia are doua radacini reale: x1:', x1, 'si x2:', x2)
elif d == 0:
    x = -b / (2*a)
    print('raspuns ex.2: Solutia are o singura radacina reala:', x)
else:
    print('raspuns ex.2: Solutia nu are radacini reale')

# 3.sa se scrie un algoritm care rezolva regula de 3 simpla

# 73 .... 25%
# x ..... 75%

v1 = 73
proc1 = 25
proc2 = 75
x = proc2 * v1 / proc1

print('raspuns ex.3:', x)

# 4.sa se scrie un algoritm care calculeaza aria unui cerc daca se stie raza acestuia
# aria cercului = π*R**2
# aria_cercului = x

R = 30
π = 3.14
x = π*R**2

print('raspuns ex.4:', x)

# 5. sa se scrie un algorit care calculeaza volumul unui cub cu latura cunoscuta
# volumul cubului = L**3
# volumul cubului = x

L = 5
x = L**3

print('raspuns ex.5:', x)

# 6.sa se scrie un algoritm care calculeaza volumul unei sfere daca se cunoaste raza acesteia
# volumul sferei = 4/3 * π * R**3
# volumul sferei = x

pi = 3.14
R = 3
x = 4/3 * pi * R**3

print('raspuns ex.6:', x)
"""
Operadores de comparación
"""

A = 21
B = 10
C = 0

if A == B:
    print('A == b')
else:
    print('A no es igual a B')

if A != B:
    print('A no es igual a B')
else:
    print('A es igual a B')

print(A < B)
print(A > B)

ES_MAYOR = A > B
print(type(ES_MAYOR))

print(A <= B)
print(A >= B)
print(A is B)

D = 5
F = 4
print(D is F)
print(D is not F)
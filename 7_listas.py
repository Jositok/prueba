"""
ejemplos para trabajar con listas
"""

LIST = [1, 2, 3, 4, 5, 'seis']
print(LIST)
print(LIST[0])
print(LIST[4])
print(LIST[2:5])
print(LIST[:3])
print(LIST[2:])

SIZE = len(LIST)
print('El tamaño de la lista es ', SIZE)

del LIST[2]
print(LIST)

LIST[2] = 'TRES'
print(LIST)

#Concatenar listas

LIST += ['ocho', 9, True, False]
print(LIST)

#Añadir un elemento a una lista

LIST.append('elemento nuevo')
print(LIST)

LIST.remove(False)
print(LIST)

LIST.reverse()
print(LIST)

LIST.reverse()
print(LIST)

LIST.insert(3, 'cuatro')
print(LIST)

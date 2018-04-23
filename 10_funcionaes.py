"""
Ejemplos de funciones
"""

def saludar():
    print('HOLA')

saludar()

def hi(name):
    print('hola', name)

hi('Jose')

def add_name(the_list, name):
    the_list.append(name)
    print(the_list)

L = ['Patricia', 'Carlos']
add_name(L, 'Cristina')
add_name(L, 'Paco')

def say(word):
    word = 'cambio'
    print(word)

say('hola amigos')
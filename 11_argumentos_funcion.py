"""
Diferentes maneras de usar argumentos
"""

#Argumentos posicionales

def hi(name):
    print('hola ', name)

#hi() Así fallaría porque hay que pasarle el name


#Valores por defececto

def f(n='uno'):
    print(n)

f()
f(2)

def f2(one, two, three=3):
    print('one:', one, 'two:', two, 'three:', three)

f2('pepe', 'lola')


#Usar argumentos con Keyword

f2(
    three='Carmen',
    one='Pedro',
    two='SAra',
)

def f3(name, *args):
    print('hola', name)
    print(args)

f3('Jose', 20, 30 , 60)

t = ('Jose', 20, 30 , 60)

f3('Loli', t)

def f4(*args):
    print(args)

f4('Jose', 20, 30 , 60)

def f5(**kwars):
    print(kwars)

f5(nombre='diego', edad='37')
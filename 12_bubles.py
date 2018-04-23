"""
Bucles
"""

def print_all(*args):
    for n in args:
        print(n)

print_all('pera', 'manzana', 'limón')


def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print('{}, {}'.format(count, thing))

print_all_with_position('pera', 'manzana', 'limón')


count = 0
while True:
    count +=1
    print(count)
    if(count == 100):
        break


def show_keywords_arguments(**kwars):
    for name, value in kwars.items():
        print('{}: {}'.format(name, value))

show_keywords_arguments(name='Jose', age='30')
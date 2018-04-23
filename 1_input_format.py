"""
Ejemplo para pedir imput de ususario y formatear la respuesta
"""

PREGUNTA = '¿Cómo te llamas? '
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿cómo estás?')

SALUDO =  'Bienvenido al curso de Python'
RESPUESTA_FORMATEADA = 'Hola {}, {}'.format(RESPUESTA, SALUDO)

print(RESPUESTA_FORMATEADA)
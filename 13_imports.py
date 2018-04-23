"""
Ejemplos de como importar modulos y funciones
"""

import utils

utils.sumar(6, 8)
utils.restar(10,4)

from utils import sumar

sumar(5, 2)


from libs import bombing
bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs
where_are_the_bombs()

from libs.bombing import where_are_the_bombs, explosion
explosion()
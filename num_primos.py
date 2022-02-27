from doctest import ELLIPSIS_MARKER
import numbers

import math

def prime_checker(number):
    cont = 0

    for x in range(1, 100):
        if (n == 1) or (n % x == 0):
            cont += 1
    
    if cont > 2:
        print("No es primo")
    else:
        print("Es primo")

n = int( input("Check any of the code below: ") )
prime_checker(number=n)
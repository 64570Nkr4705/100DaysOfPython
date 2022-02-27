from itertools import combinations
from math import comb
from socket import CAN_BCM_RX_TIMEOUT
from time import CLOCK_PROCESS_CPUTIME_ID


name1 = input("Ingrese su nombre: ")
name2 = input("Ingrese otro nombre para comprobar su compatibilidad: ")

combinacion = name1 + name2
lower_case = combinacion.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e
#convertimos en string para convertir los numeros en caracteres y que se puedan concatenar
love_score = int( str(true) + str(love) )

if (love_score < 10) or (love_score > 90 ):
    pritn(f"Your score is{love_score}, you go together like coke and mentos.")
elif (love_score <= 40) or (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
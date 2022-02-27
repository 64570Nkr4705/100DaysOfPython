import random

print("***Welcome to the PyPassword Generator!***")
x = int( input("How many letters would you like un your password?\n") )
y = int( input("How many symbol would you like?\n") )
z = int( input("How many number would you like?\n") )

varand = x + y + z

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '#', '$', '%', '&', '/', '=', '?', '¡',
'~', '¿', '*']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
password = ''

for s in range(0, x):
    pos = random.randint(0, 26)
    password += letters[pos]
print(password)

for s in range(0, y):
    pos = random.randint(0, 11)
    password += symbols[pos]
print(password)

for s in range(0, z):
    pos = random.randint(0, 9)
    password += numbers[pos]
print(password)

#con esto convierto el password generado en una lista separando cada caracter individualmente
passwordG = list(password)

passwordO = ''

for s in range(0, len(password)):
    pos = random.randint(0, len(password) -1)
    passwordO += passwordG[pos]
print(passwordO)
'''
#otra forma es usar 'random.choise()
passw = []
for s in range(0, x):
    #elegira aleatoria mente elementos de una lista
    #se podria escribir de la siguiente manera:
    #passw.append.(random.choice(letters))
    passw += random.choice(letters) 
for s in range (0, y):
    passw += random.choice(symbols)
for s in range(0, z):
    passw += random.choice(numbers)
print(passw)
random.shuffle(passw)
print(passw)

#otro metodo es:
pas = ''
for s in passw:
    pas += s
print(f"Your passowrd is: {pas}")
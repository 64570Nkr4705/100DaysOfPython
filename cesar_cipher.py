
from multiprocessing.context import SpawnContext


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text0 = input("Type your message:\n").lower()
shift = int( input("Type the shift number of 1 - 26:\n") )

text = list(text0)
#codex = ''
#decodex = ''

def func_encode(word, space):
    codex = ''

    #recorrere los caracteres del texto que se ingrese por teclado
    #al incorporar un rango en el for, la 'i' dara un numero entero
    #al llamar a una cadena de caracteres, la 'i' dara un caracter o elemnto
    for i in range(len(word)):
        
        if word[i] == ' ':
            codex += word[i]
        #en el elif puse "elif (pos + space) >= len(letters)
        elif (letters.index(word[i]) + space) >= len(letters):
            planb = (letters.index(word[i]) + space) - len(letters)
            codex += letters[planb]
        else:
            #guardara en una variable 'pos' la posicion donde se encuentre mi caractere en la lista 'letters'
            pos = letters.index(word[i])
            #se guaradarn los caracteres en una variable 'codex' la cual obtendre por la variable 'pos' + el numero ingresado por teclado
            codex += letters[pos + space]
    print(codex)

def func_decode(word, space):
    decodex = ''
    
    for i in range(len(word)):

        if word[i] == ' ':
            decodex += word[i]
        elif (letters.index(word[i]) - space) <= letters.index('a'):
            planb = (letters.index(word[i]) - space) + len(letters)
            decodex += letters[planb]
        else:
            pos = letters.index(word[i])
            decodex += letters[pos - space]
    print(decodex)

if direction == 'encode':
    func_encode(word=text, space=shift)
else:
    func_decode(word=text, space=shift)


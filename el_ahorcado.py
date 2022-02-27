import random

palabras = ['mouse', 'holaword']
#elegira un elemento de la lista al azar
selec = random.choice(palabras)
#convertira el elemento seleccionado en una lista
list_selec = list(selec)
#sera la palabra anonima
selec2 = list()

#recorrera la lista vacia y la rellenara de guiones bajos
while len(selec2) < len(list_selec):
    selec2 += '_'
print(selec2)

vida = 0
lugares = 0


while (vida < 6) and (lugares < len(selec)):
    x = input("Ingrese la letra de la palabra: ")
    pos = 0
    modf = 0
    esp = 0

    #ir sustituyendo la s por cada caracter de la variable selec
    for s in selec:
        #Comapara s con x siendo 'x' el caracter ingresado por taclado
        if s == x:
            #si el caracter coincide con el ingresado tomara la posicion que le corresponda
            selec2[pos] = x
            lugares += 1
            esp += 1
            
        pos += 1
    if modf == esp:
        vida += 1
        
    print(selec2)
    print(lugares)

if vida == 6:
    print("Game Over!")
elif lugares == len(selec):
    print("You Win!")
        





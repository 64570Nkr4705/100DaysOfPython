
apuesta = []
apos = {}
respuesta = 'si'

while respuesta == 'si':
    name = input("What is your name?: ")
    ap = input("cual es su puja: $")
    
    apos = {name : ap}

    apuesta.append(apos)

    
    respuesta = input("Hay otro participante? ")

print(apuesta)
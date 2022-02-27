print("Que desea ordenar?")
print("Samall pizza: $15")
print("Medium pizza: $20")
print("Large pizza: $25\n")

print("Pepperoni for Small pizza: +$2")
print("Pepperoni for Medium pizza: +$3\n")

print("Extra cheese for any size pizza: +$1")

costo = 0

var = input("Ingrese su pedido: ")

if var == "s":
    costo = 15
    extra = input("Desea agregar pepperoni? ")
    if extra == "y":
        costo += 2
elif var == "m":
    costo = 20
    extra = input("Desea agregar pepperoni? ")
    if extra == "y":
        costo += 3    
else:
    costo = 25

extra_cheese = input("Deea agregar queso extra? ")
if extra_cheese == "y":
        costo += 1

print(f"costo total a pagar es de {costo}")

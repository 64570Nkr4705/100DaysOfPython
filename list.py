import random

names_str = input("Give me everybody\'s names, seperated bu a comma. ")
#Esto convertira a las cadenas ingrsadas en una lista y las separara por una comma y espacio
list_names = names_str.split(", ")
#esto devolvera la longitud de la lista
x = len(list_names)
#devolvera un valor aleatorio desde el 0 hasta la longitud max de la lista
rand = random.randint(0, x)
#imprimira el valor aleatorio de la lista de nombres
print("El elejido es: ", list_names[rand])
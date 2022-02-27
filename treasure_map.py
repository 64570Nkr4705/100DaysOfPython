#creamos 3 listas vacias
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
#anidamos las 3 listas en una sola
map = [row1, row2, row3]
#imprimimos la lista con saltos de linea, para que nos quede como una matriz
print(f"{row1}\n{row2}\n{row3}")
#pedimos que ingresen la posicion a insertar la 'X'
position = input("Where do you want to put the treasure? ") #23
#Como la posicion a insertarse ser de tipo str, la convertimos a tipo entero (int)
'''craremos dos variables para colocar a cada una la posicion de los dos digitos
caundo se ingresen por teclado, y luego se convertira a tipo entero, en este caso
seria '23str' luego nos quedaria columna 2, fila 3'''
horizontal = int(position[0]) #2
vertical = int(position[1]) #3
#a la posicion vertical se le resta uno, como el indice empieza en 0
selected_row = map[vertical -1]
#y luego se le asigna la 'x' en la posicion mencionada
selected_row[horizontal -1] = "X"
#se imprime por pantalla
print(f"{row1}\n{row2}\n{row3}")



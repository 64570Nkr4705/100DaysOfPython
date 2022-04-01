from prettytable import PrettyTable

table = PrettyTable()
#Crea columnas
table.add_column("Pokemon name", ["Pikachu", "squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "fire"])
#Se alinea a la izquierda
table.align = "l"

print(table)
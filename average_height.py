#Example: student_heights = [180, 124, 165, 173, 189, 169, 146]
student_heights = input("Input a list of student heights: ").split()
sumTotal = 0
totalElem = 0
#el bucle 'for' recorrera la lista convirtiendo a cada elemento en un entero
for n in range(0, len(student_heights) ):
    student_heights[n] = int(student_heights[n])
    totalElem += 1
    sumTotal += student_heights[n]

promedio = sumTotal / totalElem

print(student_heights)
print(promedio)

'''Tambien existe otra funcion llamada len() y sum(), la cual,
la primera nos devolvera la longitud de la lista mienstras la otra
nos devolvera la suma total de todos los elementos'''
student = input ("Ingrese la lista de estudiantes: ").split()

for x in range(0, len(student)):
    student[x] = float( student[x] )
#Se sumaran los elementos de la lista y se dividira por la cantidad de elementos
#round redondeara el resultado, dandonos un entero aproximado
promedio = round( sum(student) / len(student) )

print(student)
print(promedio)
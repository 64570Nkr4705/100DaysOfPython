'''con la funcion max() y min(), se pueden conocer los valores
maximos y minimos de una lista'''

studentScore = input("Input a list of student score: ").split()

max = 0.00
min = 9999.00

for x in range(0, len(studentScore)):
    studentScore[x] = float(studentScore[x])
    if studentScore[x] > max:
        max = studentScore[x]
    if studentScore[x] < min:
        min = studentScore[x]

print(studentScore)
print(max)
print(min)
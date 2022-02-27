total = 0

for number in range(1, 101):
    total += number

print(total)

sumPar = 0
for number in range(1, 101):
    if number % 2 == 0:
        sumPar += number

print(sumPar)
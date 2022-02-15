year = int(input("Enter a year to see if it is a leap year: "))

if year % 4 == 0 and (year % 100 != 0):
    print("El año es bisiesto")
elif year % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
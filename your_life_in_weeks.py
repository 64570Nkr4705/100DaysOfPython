year_old = int(input("Ingrese cuantos años tiene: "))
year_of_life = 90 - year_old
one_months = 12
one_week = 52
one_day = 365

days_of_life = year_of_life * one_day
week_of_life = year_of_life * one_week
months_of_life = year_of_life * one_months

print(f"A usted le quedan {days_of_life} dias, {week_of_life} semanas y {months_of_life} meses de vida!!!")

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

'''Escribo el objeto(variable), que contiene la clase, seguido de un punto
luego llamar al metodo que necesito'''
#coffee_maker.report()
#money_machine.report()

is_on = True
while is_on:
    '''Las opciontes serán iguales al objeto de menú y luego llamaremos
        al método get_items. Luego cuando este método regrese, guardará 
        la cadena y todas las opciones en esta variable llamada opciones'''
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    '''Si la elección es igual a off, entonces eso signidica que is_on 
        será igual a falso, y si la elección es igual a informar, bueno,
        es este caso vamos a obtener la cafetera y la máquina de hacer dinero
        para hacer sus informes en la consola.'''
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        '''De lo contrario, vamos a guardar nuestra bebida como una variable 
            llamada bebida, y luego vamos a acceder al menú fin_drink, 
            como notará, toma el nombre d eun pedido como entrada.
            Así que esta es una cadena y será igual a lo que el usuario eligió
            dentro de la opción choice.'''
        drink = menu.find_drink(choice)
        '''Agarremos nuestro objeto cafetera y luego comprobemos si los recursos
            son suficientes para hacer la bebida que nos interesa.'''
        if coffee_maker.is_resource_sufficient(drink):
            '''vamos a nuestra máquina de hacer dinero y luego al método 
                make_payment y tenemos que transferir el costo de la bebida.'''
            if money_machine.make_payment(drink.cost):
                '''Lo siguiente es agarrar el objeto cafetera y luego llamar
                    al metodo make_coffee y podemos pasar el orden de nuestra
                    bebida'''
                coffee_maker.make_coffee(drink)
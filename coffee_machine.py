menu = {
    #1-Espresso
    1 : {
        "ingredients" : {
            "water" : 300,
            "milk" : 200,
            "coffee" : 100,
        },
        "cost": 1.5,
    },
    #2-Latte
    2: {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    #3-Cappuccino
    3: {
        "ingredients": {
            "water": 250,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

        

    
def func_resources(order_ingredients):
    #Comapará si los recursos son suficientes para preparar el café
    for item in order_ingredients:
        #recorrera los valores del diccionario ingredientes del cafe especificado en orden
        #compará cada valor de los ingredientes si son iguales
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            #Retornara Falso si los recursos son insuficientes
            return False
    #retornara verdadero si hay recursos suficientes en la maquina
    return True


def func_coins():
    #Retornara el calculo total de las manedas insertadas
    print("Please insert coins.")
    total = int(input("how many quarters?: $")) * 0.25
    total += int(input("how many dimes?: $")) * 0.1
    total += int(input("how many nickels?: $")) * 0.05
    total += int(input("how many penies?: $")) * 0.01
    return total



def func_transaction(money_recived, order_cost):
    #Retornara verdadero si el pago es aceptado, o falso si el pago es insuficiente
    if money_recived >= order_cost:
        #devolvera el vuelto en caso de que este sea mayor al costo del cafe
        #redondeando hasta 2 decimales
        change = round(money_recived - order_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += order_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    '''Deduce los ingredientes necesarios'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your coffee ☕")
    print("Come back soon😇!!!")

on = True
while on:
    #convertir la variable orden para que otras funciones la puedan tomar
    global order
    order = int( input("What would you like drink? \n(1-espresso/2-latte/3-cappuccino/4-resources): ") )
    if order == 0:
        on = False
    #La orden 4 moistrará los recursos de la maquina
    elif order == 4:
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        #Se crea una variable bebida que contendra el diccionario con la llave especificada en orden
        drink = menu[order]
        #Se imprimira el valor de la llave
        print(drink)
        #Si la funcion recursos es verdadera
        if func_resources(drink["ingredients"]):
            #se guardara en una variable el total del dinero ingresado
            payment = func_coins()
            '''Se llamara a la funcion enviadole como parametro el total del
            dinero ingresado y el costo del cafe elegido
            Si la funcion es verdader llamara a la funcion make_coffe'''
            if func_transaction(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

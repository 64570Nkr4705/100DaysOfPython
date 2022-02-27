#Se importa el modulo random
import random

#Se pide al usuario que ingrese na posicion
x = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))

#Luego se ubica esa posicion en la lista
list = ["rock", "paper", "scissors"]
position = list[x]

rock = '''
  ____, O
   /   /M|
  /|MMMMMMMM
  {| | // |}
-_}| |/ \ |{_apx
 

'''
paper = '''
  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""     
'''
scissors = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

#se imprime por pantalla la posicion dada
print(f"Your choise was {position}\n")

#posicion aleatoria de la pc
y = random.randint(0, 3)
positionpc = list[y]

print(f"Your opponent chose {positionpc}")

if x > y:
    if y == 0:
        if x == 2:
            print("You Lost!")
        else:
            print("You Win!")
    else:
        print("You Win!")
elif y > x:
    print("You Lost!")
else:
    print("Tried!")

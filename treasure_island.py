print("WELCOME TO tREASURE iSLAND.\n Your mission is to find the treasure.")

randl = input("You\'re at a crossroad, where do you want to go? 'Right' or 'Left'?\n").lower()
if randl == "right":
    print("Game Over.")
else:
    sandw = input("swin or wait? \n").lower()
    if sandw == "swin":
        print("Game over.")
    else:
        wd = input("Which Door? (Blue - Red - Yellow)\n").lower()
        if wd == "blue":
            print("Game Over.")
        elif wd == "red":
            print("Game Over.")
        else:
            print("You Win!")
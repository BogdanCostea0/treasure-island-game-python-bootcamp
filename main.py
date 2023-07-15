# Treasure Island Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('''Welcome to Treasure Island.
Your mission is to find the treasure''')

ans = input("You got stuck on a island and the path is splitiing. Which way you chosing?(Left/Right)").lower()
if ans == "right":
    print("You fall into a hole. Game Over")
elif ans == "left":
    ans = input("You chosed the good path. Now an aligator is coming to your path? You chose to wait or swim and ran "
                "away?swim/wait").lower()
    if ans == "swim":
        print("You got attacked by a trout. Game over")
    elif ans == "wait":
        ans = input("You were patient and the aligator ran away. Now you found an old build with three doors, "
                    "which door you choose (yellow/green/blue").lower()
        if ans == "red":
            print("burned by fire. Game Over")
        elif ans == "blue":
            print("Eaten by beasts. Game Over")
        elif ans == "yellow":
            print("Good Job. You found the treasure")
        else: print("Game Over")








print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\n\n")
fork_in_road = input("You come across a fork in the road. Will you go left or right?\n")
if fork_in_road == "left" or fork_in_road == "Left":
    lake = input("You continue on the path and come across a lake. Do you wish to swim or wait for a boat?\n")
    if lake == "swim" or lake == "Swim":
        print("You get in the water. Halfway through, you are attacked by alligators and eaten. GAME OVER")
    elif lake == "wait" or "Wait":
        boat = input("You wait at the lake's shore for 5 minutes. A man in a boat approaches from the lake. He offers you a ride to the other side of the lake. Do you say yes or no?\n")
        if boat == "no" or boat == "No":
            print("You say no to him and keep waiting. You die of boredom. GAME OVER")
        else:
            print("You accept the stranger's kind act and are taken to the other side of the lake.")
            door = input("You continue down a path from the shoreline. You approach three doors.\nOne is Red, one is Blue, and the last one is Yellow. Which door do you choose?\n")
            if door == "Red" or door == "red":
                print("You open the door and are met by burning flames larger than yourself and hot magma.\nYou are sucked in by the heat and burn to death. GAME OVER")
            elif door == "Blue" or door == "blue":
                print("You open the door and are met by three massive beasts.\nThey grab you and eat you. GAME OVER")
            elif door == "yellow" or door == "Yellow":
                print("You open the door and are met with piles of treasure higher than you can see.\nYOU WIN")
            else:
                print("You keep waiting but nothing happens.")
                print("You die of boredom")
                print("GAME OVER")
    else:
        print("You keep waiting but nothing happens.")
        print("You die of boredom")
        print("GAME OVER")
elif fork_in_road == "right" or fork_in_road == "Right":
    print("You continue down the path but get attacked by snakes and bears. You die. GAME OVER")
else:
    print("You keep waiting but nothing happens.")
    print("You die of boredom")
    print("GAME OVER")

game_end = input("Press and enter any button to exit\n")
if input:
    print("bye")
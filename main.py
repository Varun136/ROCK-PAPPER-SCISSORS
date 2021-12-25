import images
import random

IMAGES = [images.rock,images.scissors,images.paper]

GAME_ON = True

while GAME_ON:

    USER_INPUT = int(input("enter your choice \n ROCK[0],SCISSORS[1],PAPPER[2] : "))

    COMPUTER_INPUT = random.randint(0,4)

    if USER_INPUT > 2 :
        print("Ooops wrong command")

    elif USER_INPUT == 0 and COMPUTER_INPUT == 2:
        print(IMAGES[USER_INPUT])
        print(IMAGES[COMPUTER_INPUT])
        print("you lost")
    elif USER_INPUT == 2  and COMPUTER_INPUT == 0:
        print(IMAGES[USER_INPUT])
        print(IMAGES[COMPUTER_INPUT])
        print("you won")
    elif USER_INPUT == COMPUTER_INPUT:
        print(IMAGES[USER_INPUT])
        print(IMAGES[COMPUTER_INPUT])
        print("its a tie")
    elif USER_INPUT > COMPUTER_INPUT:
        print(IMAGES[USER_INPUT])
        print(IMAGES[COMPUTER_INPUT])
        print("you lost")
    elif USER_INPUT < COMPUTER_INPUT:
        print(IMAGES[USER_INPUT])
        print(IMAGES[COMPUTER_INPUT])
        print("you won")


    CONTINUE = input("Do you want to play again Yes/No : ").lower()
    if CONTINUE == 'yes':
        GAME_ON = True
    else :
        GAME_ON = False
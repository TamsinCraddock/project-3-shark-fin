from text_utils import print_sharkfin_logo, print_rules, print_game_over
from game_utils import game, list_of_words
from random import choice

print_sharkfin_logo()

name = input("Welcome to sharkfin, enter your name to get started: ")
print("Hello,", name)

game_over = False
quit_game = False
won = False

while not quit_game:
    print("1. (R)ules")
    print("2. (S)tart Game")
    print("3. E(x)it")

    option = input("Enter an option: ").lower()

    if option == "r":
        print_rules()
    elif option == "s":
        word = choice(list_of_words)
        won = game(word)
        game_over = True
        quit_game = True
    elif option == "x":
        quit_game = True
    else:
        print("invalid input, try again..")

if game_over:   
    print_game_over(word, won)
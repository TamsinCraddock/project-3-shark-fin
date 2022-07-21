"""
Shark Fin Game entry point.
"""

from random import choice
from text_utils import print_sharkfin_logo, print_rules, print_game_over
from game_utils import game, get_list_of_words


def run():
    """
    Runs the game
    """
    print_sharkfin_logo()

    name = input("Welcome to sharkfin, enter your name to get started: ")
    print("Hello,", name)

    game_over = False
    quit_game = False
    won = False

    while not quit_game:
        print("1. Rules")
        print("2. Start Game")
        print("0. Exit")

        option = input("Enter an option: ")

        if not option.isnumeric():
            print("invalid choice, choose a number from the list.")
            continue

        option = int(option)

        if option == 1:
            print_rules()
        elif option == 2:
            word = choice(get_list_of_words())
            won = game(word)
            game_over = True
            quit_game = True
        elif option == 0:
            quit_game = True
        else:
            print("invalid input, try again..")

    if game_over:
        print_game_over(name, word, won)


run()

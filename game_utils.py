"""
Set of utils to control game flow

"""

import re
from text_utils import display_shark_fin, print_invalid_input, print_already_guessed
TRIES_ALLOWED = 5


def game(word):
    """
    Starts the game

    Returns:
        Bool: won or lost
    """
    tries = 0
    prompt = ""
    tempword = word
    for _ in word:
        prompt = prompt + "_"
    done = False
    win = False
    guesses = set()
    while not done:
        print(f"{prompt}\n")
        raw_guess = input("Enter a guess: ").lower()
        if not len(raw_guess) == 1 or not raw_guess[0].isalpha():
            print_invalid_input()
            continue
        guess = raw_guess[0]
        if guess in guesses:
            print_already_guessed()
            continue
        guesses.add(guess)
        indices = [i.start() for i in re.finditer(guess, tempword)]
        if len(indices) < 1:
            tries = tries + 1
            print(f"Incorrect, try again - {TRIES_ALLOWED - tries} remaining")
            display_shark_fin(tries)
            if tries >= TRIES_ALLOWED:
                done = True
            continue
        for i in indices:
            tempword = tempword[:i] + "_" + tempword[i+1:]
            prompt = prompt[:i] + guess + prompt[i+1:]
        if "_" not in prompt:
            done = True
            win = True

    return win


def get_list_of_words():
    '''
    retrieve a list of words from a specially prepared CSV file

    Returns:
        list of strings
    '''
    file_path = "words.csv"
    words = []
    try:
        with open(file_path) as file:
            for line in file:
                words.append(line.rstrip("\n"))
    except OSError as error:
        print(f"Could not read csv file '{file_path}' error - ", error)
        words = ["fallback"]
    return words

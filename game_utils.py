import re
def game(word):
    """
    Starts the game

    Returns:
        Bool: won or lost
    """
    tries_allowed = 5
    tries = 0
    prompt = ""
    tempword = word
    for _ in word:
        prompt = prompt + "_"
    done = False
    win = False
    while not done:
        print(prompt)
        raw_guess = input("Enter a guess: ").lower()
        if not len(raw_guess) == 1 or not raw_guess[0].isalpha():
            print("invalid input, please enter a single letter")
            continue
        guess = raw_guess[0]       
        indices = [i.start() for i in re.finditer(guess, tempword)]
        if len(indices) < 1:
            tries = tries + 1
            print(f"Incorrect, try again - {tries_allowed - tries} remaining")
            # make sharks move up
            if tries >= tries_allowed:
                done = True
            continue
        for i in indices:
            tempword = tempword[:i] + "_" + tempword[i+1:]
            prompt = prompt[:i] + guess + prompt[i+1:]
        if "_" not in prompt:
            done = True
            win = True

    return win


list_of_words = [
    "cheese",
    "random",
    "lamp",
    "bacon"
]

def game(word):
    """
    Starts the game

    Returns:
        Bool: won or lost
    """
    print("In game")
    prompt = ""
    # tempword = word
    for _ in word:
        prompt = prompt + "_"
    done = False
    while not done:
        print(prompt)
        guess = input("Enter a guess: ").lower()[0]
        try:

            index = tempword.index(guess)
            
        except ValueError:
            print("Incorrect, try again")

    return True


list_of_words = [
    "cheese",
    "random",
    "lamp",
    "bacon"
]

"""
Module which outputs text to screen
"""
import time
from termcolor import colored, cprint


def print_sharkfin_logo():
    """
    Logo for the game. Generated with: https://patorjk.com/
    """
    print("""

  /$$$$$$  /$$                           /$$             /$$$$$$$$ /$$          
 /$$__  $$| $$                          | $$            | $$_____/|__/          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$      | $$       /$$ /$$$$$$$ 
|  $$$$$$ | $$__  $$ |____  $$ /$$__  $$| $$  /$$/      | $$$$$   | $$| $$__  $$
 \____  $$| $$  \ $$  /$$$$$$$| $$  \__/| $$$$$$/       | $$__/   | $$| $$  \ $$
 /$$  \ $$| $$  | $$ /$$__  $$| $$      | $$_  $$       | $$      | $$| $$  | $$
|  $$$$$$/| $$  | $$|  $$$$$$$| $$      | $$ \  $$      | $$      | $$| $$  | $$
 \______/ |__/  |__/ \_______/|__/      |__/  \__/      |__/      |__/|__/  |__/





    """)


def print_rules():
    """
    Displays the game rules
    """
    print("""
1. The game will automatically generate a random word.
2. The amount of letters that the word contains is shown by the amount of blank tiles.
3. Guess one letter in each turn.
4. If you guess a correct letter that the word contains, the letter will display on the relevant tiles within the word.
5. If the guess is correct, the shark will remain in the same position and you can guess another letter.
6. If the guess is incorrect, the shark fin will move one step closer to the swimming person.
7. Once the shark fin reaches the swimming person, you lose.
8. Good luck!
    """)


def print_already_guessed():
    cprint("\nAlready guessed, try again\n", "yellow")


def print_invalid_input():
    cprint("\ninvalid input, please enter a single letter\n", "yellow")


def print_game_over(name, word, win=False):
    """
    Displays the game over message
    """
    if win:
        cprint("""


     /$$     /$$                        /$$      /$$ /$$           /$$
    |  $$   /$$/                       | $$  /$ | $$|__/          | $$
     \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$ | $$
      \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$| $$
       \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$|__/
        | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$    
        | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$ /$$
        |__/  \______/  \______/       |__/     \__/|__/|__/  |__/|__/



        """, "green")
        cprint(f"You correctly guessed the word '{word}'! You win, {name}!\n", "green")
    else:
        cprint("""



     /$$     /$$                        /$$                                     /$$
    |  $$   /$$/                       | $$                                    | $$
     \  $$ /$$//$$$$$$  /$$   /$$      | $$        /$$$$$$   /$$$$$$$  /$$$$$$ | $$
      \  $$$$//$$__  $$| $$  | $$      | $$       /$$__  $$ /$$_____/ /$$__  $$| $$
       \  $$/| $$  \ $$| $$  | $$      | $$      | $$  \ $$|  $$$$$$ | $$$$$$$$|__/
        | $$ | $$  | $$| $$  | $$      | $$      | $$  | $$ \____  $$| $$_____/    
        | $$ |  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/ /$$$$$$$/|  $$$$$$$ /$$
        |__/  \______/  \______/       |________/ \______/ |_______/  \_______/|__/


            """, 'red')
        cprint(f"Sorry {name}, you lost... The word was '{word}'.\n", 'red')


def display_shark_fin(step=1):
    """
    Displays the shark fin moving towards the victim
    """
    if step == 2:
        print("""
                        @                                                          @@@@@@@@@
                      @@ @@                                                       @@@@@@@@@@@
                     @@    @@                                                  @@@
                    @@     @@                                                  @@@     @@
       ,(         @@  ,(    @@        ,(              ,(              ,(        @@    @@@@@
;,,..,`..--.'`.;.--.'`..--.'  `..--.'`..--.'  `..--.'`..--.'  `..--.'`..--.'  `.@@-.'.,@@@,.,.,.,..
        """)
    elif step == 3:
        print("""
                                        @                                         @@@@@@@@@
                                      @@ @@                                       @@@@@@@@@@@
                                     @@    @@                                  @@@
                                    @@     @@                                  @@@     @@
             ,(             ,(     @@       @@,(              ,(              ,(  @@    @@@@@
;,,..,`..--.'`...--.'`..--.'  `.-;-.'`..--.'  `..--.'`..--.'  `..--.'`..--.'  `.@@-.'.,@@@,.,.,.,..
        """)
    elif step == 4:
        print("""
                                                       @                           @@@@@@@@@
                                                     @@ @@                        @@@@@@@@@@@
                                                    @@    @@                   @@@
                                                   @@     @@                   @@@     @@
             ,(             ,(              ,(    @@       @@,(             ,(  @@    @@@@@
;,,..,`..--.'`...--.'`..--.'  `.--.'`..--.'  `..;--.'`..--.'  `..--.'`..--.'  `.@@-.'.,@@@,.,.,.,..
        """)
    elif step == 5:
        print("""
                                                                        @          @@@@@@@@@
                                                                      @@ @@       @@@@@@@@@@@
                                                                     @@   @@   @@@
                                                                    @@    @@   @@@     @@
             ,(             ,(             ,(               ,(    @@       @@,( @@    @@@@@
;,,..,`..--.'`...--.'`..--.'  `.--.'`..--.'  `..;--.'`..--.'  `..--.'`..--.'  `.@@-.'.,@@@,.,.,.,..
        """)
        time.sleep(0.75)
        print("""
                                                                                          @                   
                                                                                        @@ @@                  
                                                                                       @@   @@      
                                                                                      @@    @@             
              ,(               ,(             ,(             ,(               ,(    @@       @@,(            
;--.'.'`..--.'  `.;,,..,`..--.'`...--.'`..--.'  `.--.'`..--.'  `..;--.'`..--.'  `..--.'`..--.'  `. 
        """)
    else:
        print("""
         @                                                                         @@@@@@@@@
       @@ @@                                                                      @@@@@@@@@@@
     @@    @@                                                                  @@@
   @@      @@                                                                  @@@     @@
 @@    ,(   @@        ,(              ,(              ,(              ,(        @@    @@@@@
;,,..,`..--.'  `..--.'`..--.'  `..--.'`..--.'  `..--.'`..--.'  `..--.'`..--.'  `.@@-.'.,@@@,.,.,.,..
        """)

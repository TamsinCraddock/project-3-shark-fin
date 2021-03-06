# **Shark Fin**

Shark Fin is a word challenge game. A simple game that is played in the command line. 

This game is a modern take on the traditional 'Hangman' version. 

The aim of the game is to guess a random word by entering one letter at a time. You have a limited number of attempts. If you manage to guess the correct word before you run out of attempts, you win, otherwise the shrk catches you and you lose.

The game concept is simple, but it is a challenging game. It's a great way to sit back, relax and challenge yourself. Enjoy!

![Shark Fin game display](assets/images/shark-fin-responsiveness-layout.png)

---

## **Contents:**
- [User Experience:](#user-experience)
    - [User Requirements:](#user-requirements)
        - User stories
        - Owner goals
        - How Shark Fin works
    - [Wireframes/ Flowchart:](#Wireframes/Flowchart)
    - [Design](#design)
- [Features:](#features)
    - [Existing Features:](#existing-features)
        - Start
        - Menu
        - Rules of the game
        - Playing the game
        - Guessing the same letter
        - End of game
    - [Future features:](#future-features)
- [Technologies used:](#technologies-used)
    - [Main language](#main-language)
    - [Other Frameworks, Libraries and Software Used](#other-frameworks-libraries-and-software-used)
- [Testing:](#testing)
    - [Manual testing](#manual-testing)
    - [Input validation](#input-validation)
    - [Validator testing](#validator-testing)
- [Bugs:](#bugs)
    - [Solved](#solved)
    - [Left to solve](#left-to-solve)
- [Deployment:](#Deployment)
- [Credits:](#Credits)

----

## **User Experience:** 
### User requirements:

#### **User stories**

As a user, I expect:
- to understand how the game works quickly.
- the program to be simple to use and easy to understand.
- feedback while playing the game.
- to be able to restart the game easily.
- text that is easy to read.
- color that helps me understand the feedback.
- to be able to access the game rules easily.

### Owner goals:

As a owner, I aim to:
- provide a program that fulfils the users' needs.
- create a game that is easy to use & understand.
- create an experience that is pleasant for users.

### How Shark Fin works:
- The program chooses one word randomly from the list with 2500 different words.
- The word is presented as dashes, one for each letter in the word.
- It is only allowed to guess one letter at a time. The Shark Fin dosn't move forward if it's a correct guess.
- When the players guess is wrong, the game will notify the player and the Shark Fin graphic will change to be one step closer to the swimming person. 
- The player wins when the word is guessed and all lives are not lost. A message will display.
- The player loses if the lives runs out. A message will show to tell the game is over.
- When the game is finished the player can choose to restart, or otherwise return to the starting screen.


## **Wireframes/ Flowchart:**
As this game only is played in the terminal, no wireframes for the visual was done before the project started. I did a simple flowchart to guide me through the coding and to get a map for how I wanted it to work.

![Shark Fin game plan flow chart](assets/images/sharkfin-flow-chart.jpg)

## **Design:**
The program has been designed based on the five planes of content strategy. Although it is a terminal application and therefore differs somewhat from web design, each plane still applies in some way.

The design is very limited due to the game being played through the terminal. I have put some color and ASCII-art in it to add to the overall design and user experience. This also helps with the user feedback as the text colour used changes dependingon the game output.

## **Features:**
### Existing Features:

#### Start: 
When you start the game you will be able to enter your name. This is for personal feedback through the game.

 ![Shark Fin game start](assets/images/shark-fin-game-start.png)

 #### Menu: 
 In the next step you have three choices: \
 1 . Rules \
 2 . Start Game \
 0 . Exit

 ![Shark Fin game menu](assets/images/shark-fin-game-menu.png)

 #### Rules of the game:
 A short explanation of the rules and how to play the game is displayed. The user will also have the option to choose how they would like to proceed following reading or the rules. They will either be able to start the game or exit.

Rules of the game:
1. The game will automatically generate a random word.
2. The amount of letters that the word contains is shown by the amount of blank tiles.
3. Guess one letter in each turn.
4. If you guess a correct letter that the word contains, the letter will display on the relevant tiles within the word.
5. If the guess is correct, the shark will remain in the same position and you can guess another letter.
6. If the guess is incorrect, the shark fin will move one step closer to the swimming person.
7. Once the shark fin reaches the swimming person, you lose.
8. Good luck!

 ![Shark Fin game rules](assets/images/shar-fin-game-rules.png)

 #### Playing the game:
 - When playing the game, the letter guessed will be placed on the blank tile/s where relevant when the guess is correct. 

![Shark Fin correct guess display](assets/images/shark-fin-correct-guess.png)

- If you guess wrong, it will notify you in red text along with a graphic of the shark fin moving closer to the swimming person.

![Shark Fin incorrect guess](assets/images/shark-fin-incorrect%20guess.png)

#### Guessing the same letter:

- If you guess same letter more than once you will be notified in yellow text. No lives is withdrawn and you can try again.

![Shark Fin same letter guessed warning message](assets/images/shark-fin-same-letter-guessed-warning.png)

#### End of game:
- When game is finished you will be greeted with different graphics depending if you win or loose.

![Shark Fin win message](assets/images/shark-fin-win-message.png)

![Shark Fin lose message](assets/images/shark-fin-you-lose.png)

### Future Features:
- Add levels of difficulty.
- Add a multiplayer option.
- Add more graphics and possibly a background image instead of a plain background.

-----

## **Technologies Used:**
### Main Language:
- Python

### Other Frameworks, Libraries and Software Used:
- [Heroku](https://dashboard.heroku.com) is used to deploy the live app version.
- [Drawio](https://app.diagrams.net/) was used to create the game funcionality plan and flowchart.
- [Termcolor 1.1.0](https://pypi.org/project/termcolor/) was used to create the colours within the game.
- [Github](https://github.com/) is used for source control.
- [Gitpod](https://gitpod.io) was used to create all files & code.

-----

## **Testing:**
### Manual Testing:
This project has been tested manually for the most part. Mostly by myself playing it over and over again to make sure the logic worked. Manual testing was also done for making sure I got necessary feedback while playing, and that the feedback was presented in a clear way.

I also asked two friends to test the game to get an outside opinion on the functionality and the flo of the game.

### Input Validation:

- When choosing 1 or 2 in the menu, it validates that the user entered a valid input. If you put something else in it will tell you that you need to choose 1 or 2.

![Shark Fin invalid choice](assets/images/shark-fin-invalid-choice.png)

- When guessing letters it validates that the input is one letter and nothing else.

![Shark Fin invalid option input](assets/images/shark-fin-invalid-option-input.png)

- If you guess same letter twice you will be notified and will be able to try again.

![Shark Fin letter already guessed warning](assets/images/shark-fin-letter-already-guessed.png)

### Validator Testing:
The code has been tested with [PEP8](http://pep8online.com/) online. 

Initially I obtained a large number of "line too long" errors & "trailing whitespace" errors.

![PEP8 errors](assets/images/text-utils-errors-1.png)
![PEP8 errors 2](assets/images/text-utils-errors-2.png)

I spent some time adjusting the code so that the lines were shorter than 80 characters and was able to adjust the ASCII art without affecting the way it displayed. 

The code then passed through the validator successfully.

The validator also highlighted use of anomylous backslashes in the ascii art, as they were not valid escape sequences.  This was fixed by prefixing the strings with 'r' to ignore escape sequences.

![PEP8 initial errors](assets/images/text-utils-no-errors.png)

------

## **Bugs:**
### Solved:
- Incorrect colour output for valid data inputs.
- Words pulled from the words.csv included new line.
- Exit key stopped working after adding 'try again'option.
- Shark Fin Ascii art was displaying a duplicate of the same picture at times in the terminal. This was caused by an 'if' instead of using 'elif'.
- Ascii art was too long to display correctly - this had to be manually adjusted.
- The word space placeholders were displaying too closely togethe, making it look like one single line.
- The letter already chosen feature wasn't running correctly initially.

### Left to solve:
To the best of my knowledge, the program does not have any current bugs.

----

## **Deployment:**
- This application is deployed using Heroku. 
    https://shark-fin.herokuapp.com/


----
## **Credits:**
- The Shark Fin game logo was generated using https://patorjk.com/
- The list of 2500 random words used was taken from https://www.randomlists.com/
- The flowchart diagram for the game functionality was drawn using https://app.diagrams.net/ 
- The colour library used is from Termcolor 1.1.0 https://pypi.org/project/termcolor/
- Github used for source control https://github.com/
- The [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) on GitHub was used to develop this project. This template was designed by [Code Institute](https://codeinstitute.net/ie/) to provide a terminal that can be viewed in the browser.
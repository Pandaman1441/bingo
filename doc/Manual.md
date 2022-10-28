# Bingo! User Manual  	         	  


## Running The Program
*   To run the Bingo! Deck Generator program, simply input the following command into your terminal.
```
$ python src/bingo.py
```
*   Once you enter that in your command line the program will start and you will be prompted with a menu we will go over in the next section.

## Menu And Functionality
*   In the menu you will be prompted to enter the letter C or X.
    *   Inputting X will exit the program.
    *   Inputting C will start the process to create a new bingo deck, and you will be prompted with a series of questions about the specification of the bingo deck you want to create.
        *   The following prompts will ask for integers with ranges given in the prompts, these prompts will ask for the size of cards you would like, how many bingo cards you would like in your deck, and the highest number you would like to appear on the cards.
        *   If you input an integer outside of the given bounds then you will be asked again for whichever step you were on.
    *   If neither X or C is inputted then you will asked again to input a valid command.
*   After inputting the specifications for your bingo deck you be shown a new deck menu where you can view a specific bingo card, view all bingo cards in the deck, save the bingo deck to a file, return to the main menu, or exit the program.
*   The following are valid inputs for the deck menu.
    *   Inputting P will display a card of your choice.
        *   You will be prompted for which card you would like to view.
    *   Inputting D will display all cards in the bingo deck in numeric order.
    *   Inputting S will save the bingo deck you created to a file.
        *   You will be prompted for a file name to save the bingo deck to.
    *   Inputting R will return you to the main menu where you can choose to create a new deck.
    *   Inputting X will exit the program.

*   Any time you are prompted for a letter the program recognizes upper or lowercase letters.
## Common Errors and How to Fix Them
*   The most common error you run into is invalid inputs.
*   Invalid inputs can be any of the following.
    *   Inputting P, D, S, or R in the main menu will not work as only C and X are valid inputs in the main menu.
    *   Inputting C in the deck menu will not work as only P, D, S, R, and X are valid inputs in the deck menu.
    *   Inputting any character other than the ones specified on the menus will return you the menu and ask for a valid command.
    *   For any integer inputs only integers within the bounds given are valid.
        *   Writing out integers such as "one", or "three" are also invalid



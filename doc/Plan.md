# Software Development Plan

## Phase 0: Requirements Specification *(10%)*


##  Instructions
*   This Program will create a deck of bingo cards, the deck will have however many cards the users asks for and the cards will be of a size specified by the user as well. Once the deck of bingo cards are created the user will be able to look at individual cards, all the cards, and print the deck to a file the user provides.

##  Requirements
*   The program will open will a user interface asking the user if they want to create a bingo deck or exit the program.
    *   If they want to create a bingo deck
        *   They will be shown another menu asking for how many cards should be created, ranging from 2 to 8192.
        *   Then the size for the cards ranging from 3 to 16.
        *   Then the user will be asked for the maximum number that can appear in the deck, ranging from 2 * the size inputted to 3.9 * the size inputted.
        *   After these inputs the program will create the bingo deck to the users specifications but will ask the user if they want to print a specific card, display the whole deck, save the deck to a file, or return to the main menu.
            *   The menu will reappear after any option is inputted, except if return to the main menu is inputted in which it will start from the beginning.
    *   If the user inputs that they want to exit the program it will break and close.
        *   I think I'll try to put a exit message with a second to see it.3
*   The program will erase bingo decks that are not saved to files, when a new deck is created the previous is erased.

##  Concerns
*   Currently I'm only worried about the bug in the randomNumberSet class because I can't find it immediately but hopefully it will be clearer once I write some code and see how the class works more in depth instead of just looking at it and of course I'll run the tests myself but I'll probably fix the bug in the testing phase.
*   I'm going to have to look at other examples of UML class diagrams to get a better understanding of them.
*   For the actual program I'm mainly worried if I remember how to make user interfaces and using classes correctly.

## Phase 1: System Analysis *(10%)*


##  Inputs
*   Inputs will vary as the user continues through the program, some will be commands for the program to do and some will turned into variables to use in the program methods.
*   Once the bingo deck is created there will be an option for the user to input a file to print the bingo deck to, like stdout to the file name given.
##  Outputs
*   After the specifications are inputted there will be a menu where the program can output different things.
    *   The program will be able to print a specified bingo card from the deck created
    *   The program will be able to display the entire bingo deck
    *   The program will be able to print the bingo deck to a file.

Card class Analysis
```
class Card(size, random number set)
DESCRIPTION:
    This class will create bingo cards using the size value to determine width and height of the card. the random number set will be a list of numbers to use in the card
PARAMETERS:
    size : int
    randNumberSet : list
        The size will be the input received from the createDeck method in the userInterface class, the random number set is created from the RandNumberSet class
RETURNS:
    This class will return a bingo card with size specified by the user with unique numbers from a range specified by the user.
```

Deck class Analysis
```
class Deck(size, dSize, maxNum)
DESCRIPTION:
    This class calls the Card class to create a card then the Deck class stores the card in a list.
PARAMETERS:
    size : int
        This will be sent to Card to create a card of that size
    dSize : int
        This will be how many cards are created
    maxNum : int
        This will be the highest possible number used in card creation
RETURNS:
    This class returns a list with a however many cards the user asked for
```

__CreateDeck method Analysis
```
def __CreateDeck()
DESCRIPTION:
    This method will make the user interface for creating the bingo deck, it will ask for the specifications then send the results to deck.
PARAMETERS:
    input : int
        These will be the size of the card, size of the deck, and the number range for the cards.
RETURNS:
    Returns the users inputs as variables and sends them to classes to create the deck
```

## Phase 2: Design *(30%)*


Card
```
class card():
    def init(idnum, cardSize, ns)
        set all the variables to private

    def id()
        return idnum

    def number_at(row, col)


    def len()
        return cardSize

    def str(size, ns)
        cardFormat = "+"
        for size
            cardFormat + "-----+"
        cardFormat + \n
        for size
            cardFormat + '|'
            for size
                if size % 2 does not equal 0
                    cardFormat + "FREE!"
                else:
                    cardFormat + ns[i * size + j]
                cardFormat + '|'
            cardFormat + \n
            cardFormat + "+"
            for size
                cardFormat + "-----+"
        return cardFormat
```

Deck
```
class Deck():
    def init(self, cardSize, deckSize, numMax)
        set all the variables as private
        deck = []
        for however many cards are in the deck
            card = card(cardSize, RandNumberSet(cardSize, numMax))
            deck append with card
        return deck

    def len()
        return deckSize

    def getitem(n)
        card = ''
        n -= 1
        if n is less than or equal to deckSize
            card = deck[n]

    def str()
        return deck
```

__createDeck()
```
cardSize = input("Enter the size of the cards ", 3, 16)
numMax = input("Enter max number for the bingo cards ", card size^2 * 2, card size^2 * 3.9)
deckSize = input("Enter how many cards should be in the deck ", 2, 8192)

cDeck = deck(cardSize, deckSize, numMax)

deckMenu()
```

## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

##  Translating
*   Started implementation and almost immediately I realized that I was missing stuff and that I didn't fully understand the start code, I'm going to redo my UML class diagram and make some new methods so I can understand it better.
*   Decided to start with the  user interface modules and I don't know why I thought it was just the create deck method missing.
*   I think my user interface class looks good but create deck or something in deck or card are messed up.


##  Post Translation
*   add my new UML diagram and now I'm just running bingo and working through the errors, I've written all the code I think I need and I'm able to get to the deck menu but I can't print.
*   Once I can run bingo and do all the options I'll start testing and debugging, right now I consider the program not finished
*   Current problem I'm stuck on is trying to use the printCard method in user interface, I keep getting a type error that int object is not callable. gonna trying working on another part for a bit.
*   my getCard method is causing me problems i don't know how to fix, maybe it has to do with the time.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.

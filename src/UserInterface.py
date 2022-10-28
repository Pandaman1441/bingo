#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       

from math import floor  	    	       
import sys
import Deck  	    	       
from Menu import Menu  	    	       
from MenuOption import MenuOption  	    	       


class UserInterface():  	    	       
    """  	    	       
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	    	       

    Also provides methods for accepting and validating user input  	    	       
    """  	    	       

    def __init__(self):  	    	       
        self.__m_currentDeck = None  	    	       
        self.__m_menu = Menu("Main")  	    	       
        self.__m_menu += MenuOption("C", "Create a new deck")  	    	       
        self.__m_menu += MenuOption("X", "Exit the program")  	    	       

    def run(self):  	    	       
        """  	    	       
        Return None: present the main menu to the user  	    	       

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	    	       
        """  	    	       

        print("""
 ########   ####  ##    ##   ######     #######   ####
 ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
 ##     ##   ##   ####  ##  ##         ##     ##  ####
 ########    ##   ## ## ##  ##   ####  ##     ##   ##
 ##     ##   ##   ##  ####  ##    ##   ##     ##
 ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
 ########   ####  ##    ##   ######     #######   ####

    Welcome to the DuckieCorp Bingo! Deck Generator""")  	    	       

        while True:  	    	       
            command = self.__m_menu.prompt()  	    	       
            if command.upper() == "C":  	    	       
                self.__create_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __create_deck(self):  	    	       
        """  	    	       
        Return None: Create a new Deck  	    	       

        The Deck is stored in self.__m_currentDeck  	    	       

        """
        cSize = self.__get_int("Enter the size of the bingo cards you want. ", 3, 16)
        maxNum = self.__get_int("Enter the highest number you would like to appear on the cards. ",((cSize * cSize) * 2), floor((cSize * cSize) * 3.9) )
        dSize = self.__get_int("Enter how many cards should be in the deck. ", 2, 8192)
        self.__m_currentDeck = Deck.Deck(cSize,dSize,maxNum)
        self.__deck_menu()
        # TODO: Walk the user through the process of creating a new Deck of Cards  	    	       
        # TODO: Once a deck is made, go into the Deck menu __deck_menu  	    	       
        print("TODO: Create a Deck menu goes here\n")  	    	       

    def __deck_menu(self):  	    	       
        """  	    	       
        Return None  	    	       

        Present the deck menu to user until a valid selection is chosen  	    	       
        """  	    	       
        menu = Menu("Deck")  	    	       
        menu += MenuOption("P", "Print a card to the screen")  	    	       
        menu += MenuOption("D", "Display the whole deck to the screen")  	    	       
        menu += MenuOption("S", "Save the whole deck to a file")  	    	       
        menu += MenuOption("X", "Return to the Main menu")  	    	       

        while True:  	    	       
            command = menu.prompt()  	    	       
            if command.upper() == "P":  	    	       
                self.__print_card()  	    	       
            elif command.upper() == "D":  	    	       
                print(self.__m_currentDeck)  	    	       
            elif command.upper() == "S":  	    	       
                self.__save_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __get_str(self, prompt):  	    	       
        """  	    	       
        Return a string: non-empty input entered by the user  	    	       

        Take a prompt string as input  	    	       
        Repeat the prompt until a non-empty string is provided  	    	       
        """
        print(f"\n{prompt}")
        return input()
        pass  	    	       

    def __get_int(self, prompt, lo, hi):  	    	       
        """  	    	       
        Return an integer: validated integer input by user  	    	       

        Take a prompt string, low and high integers as input  	    	       
        Repeat the prompt until an integer that is in-range is provided  	    	       
        """
        pValid = True
        while pValid:
            print(f"\n{prompt} [{lo} - {hi}]")
            num = input()
            if num.isnumeric():
                if lo <= int(num) <= hi:
                    return int(num)

            print(f"Please enter a number in the range [{lo} - {hi}]\n")
        pass  	    	       

    def __print_card(self):  	    	       
        """  	    	       
        Return None: Print one Card from the Deck  	    	       

        Prompt user for a Card ID  	    	       
        """
        cardPrint = self.__get_int("Id of card to print", 1, self.__m_currentDeck.getDeckSize())
        if cardPrint > 0:
            print(self.__m_currentDeck.getCard(n=cardPrint))
        pass  	    	       

    def __save_deck(self):  	    	       
        """  	    	       
        Return None: Save a Deck to a file  	    	       

        Prompt user for the name of file to write the entire Deck into  	    	       
        """
        looping = True
        while looping:
            fileName = self.__get_str("Enter the file you like to save to. ")
            if fileName != "":
                f = open(fileName,"w")
                f.write()
                f.close()
                print("Saved!")
                looping = False
        pass  	    	       

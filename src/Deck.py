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

from Card import Card  	    	       
from RandNumberSet import RandNumberSet  	    	       


class Deck():  	    	       
    def __init__(self, cSize, dSize, maxNum):
        """  	    	       
        Deck constructor  	    	       
        """
        self.__cSize = cSize
        self.__dSize = dSize
        self.__maxNum = maxNum
        self.__deck = self.createDeck()


        pass  	    	       

    def createDeck(self):
        deck = []
        for i in range(self.__dSize):
            card = Card(i, self.__cSize, RandNumberSet(self.__cSize,self.__cSize * self.__cSize))
            deck.append(card)
        return deck
    def getDeckSize(self):
        """  	    	       
        Return an integer: the number of cards in this deck  	    	       

        This method was called `size` in the C++ version  	    	       
        """
        return self.__dSize
        pass  	    	       

    def getCard(self, n):
        """  	    	       
        Return Card N from the Deck  	    	       

        This method was called `operator[]` in the C++ version  	    	       
        """
        card = None
        n -= 1
        if 0 <= n < self.__dSize():
            card = self.__deck[n]
        return card

    def __str__(self):  	    	       
        """  	    	       
        Return a string: return the entire Deck as a string  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """
        for i in range(self.__dSize):
            c = self.getCard(i)
            print(c)
        pass  	    	       


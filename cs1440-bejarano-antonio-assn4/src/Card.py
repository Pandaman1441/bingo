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

import RandNumberSet
class Card():  	    	       
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	    	       

    def __init__(self, idnum, size, ns):
        """  	    	       
        Initialize a Bingo! card  	    	       
        """
        self.__idnum = idnum
        self.__size = size
        self.__ns = ns
        self.__value = [[0 for x in range(size)] for y in range(size)]
        ns.RandNumberSet.Shuffle()
        self.__card = []
        for i in range(size ** 2):
            self.__card.append(ns.RandNumberSet.next_row())
        if (size % 2 == 1):
            self.__card[(size * size) // 2] = "FREE!"
        pass

    def id(self):  	    	       
        """  	    	       
        Return an integer: the ID number of the card  	    	       
        """
        return self.__idnum
        pass  	    	       

    def number_at(self, row, col):  	    	       
        """  	    	       
        Return an integer or a string: the value in the Bingo square at (row, col)  	    	       
        """
        return self.__value[row][col]
        pass  	    	       

    def __len__(self):  	    	       
        """  	    	       
        Return an integer: the length of one dimension of the card.  	    	       
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	    	       

        This method was called `size` in the C++ version  	    	       
        """
        return self.__size
        pass  	    	       


    def __str__(self):
        """  	    	       
        Return a string: a neatly formatted, square bingo card  	    	       

        This is basically equivalent to the `operator<<` method in the C++ version  	    	       
        """
        cardFormat = "+"
        for i in range(self.__size):
            cardFormat += "-----+"
        cardFormat += "\n"
        for i in range(0, self.__size):
            cardFormat += "|"
            for j in range(0, self.__size):
                if self.__size % 2 != 0 and (i * self.__size + j) == int(pow(self.__size, 2) /2):
                    cardFormat += "{:^5}".format("FREE!")
                else:
                    cardFormat += str("{:^5}".format(self.__ns[i * self.__size + j]))
                cardFormat += "|"
            cardFormat += "\n"
            cardFormat += "+"
            for k in range(self.__size):
                cardFormat += "-----+"
            cardFormat += "\n"
        return cardFormat

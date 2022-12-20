# Roman_numbers_py
This program converts roman numbers to arabic numbers using a dictionary that contains both the roman number and its value. Also, control flow is used with a for loop and an if statement.

## Dictionary "romanNumber"

We create a _dictionary_ that contains the values of each roman number (letters from I to M) in arabic values (regular numbers)

## Function "converter"

This function iterates through a string of characters (roman number in the form "MMCVI" in example) then it _appends_ each letter in a list called "lista" which returns as a result.

## Function "calcNum"

The function calcNum uses 2 variables, which are set to 0 at the beginning. Using a _for loop_ iterates through the _range_ of the _list_ called "lista". 
It uses _reverse_ in order to iterate from right to left of the list. Then, using an if-else statement makes the most important part of the program:
In order to calculate the value of the sum of the list (which is equal to the value of the roman number), the program compares the value of one roman number to the adyacent roman number (to the left) this is expressed by: (num >= prev). In  case that comparisson results in the number on the left being greater than the one on the right, the number on the left is added. If the number on the left is less than the number on the right, then this number will be substracted to the total. The total that results from doing this operations is equal to the roman number.

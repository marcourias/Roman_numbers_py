print(f'\nConversor from Roman number to arabic numbers')
s = input("\n\nInput a Roman number: \n")

# We create a dictionary that contains the values of each roman number (letters from I to M) in arabic values (regular numbers)
romanNumber = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "C" : 100,
    "M" : 1000,
}

# The function converter iterates through a string of characters (roman number in the form "MMCVI" in example) then it appends each letter in a list called "lista"
def converter(dict, s):
    lista = []
    for char in s:
        print(dict[char])
        lista.append(dict[char])
    return lista

# The function calcNum uses 2 variables, which are set to 0 at the beginning. Using a for loop iterates through the range of the list called "lista". 
# It uses reverse in order to iterate from right to left of the list. Then, using an if-else statement makes the most important part of the program:
# In order to calculate the value of the sum of the list (which is equal to the value of the roman number), the program compares the value of
# one roman number to the adyacent roman number (to the left) this is expressed by: (num >= prev). In  case that comparisson results in the number
# on the left being greater than the one on the right, the number on the left is added. If the number on the left is less than the number on the right,
# then this number will be substracted to the total. The total that results from doing this operations is equal to the roman number.

def calcNum(lista):
    sum = 0
    prev = 0

    for i in reversed(range(len(lista))):
        num = lista[i]
        if num >= prev:
            sum += num
        else:
            sum += -num
        prev = num
        #print(f"La suma en la iteración es: {sum}")

    print(f"The roman number '{s}' is: {sum} in arabic numbers.")
    print(f"The list of numbers used to calculate {sum} was:\n {lista}")    
    return sum

            


lista = converter(romanNumber, s)
suma = calcNum(lista)




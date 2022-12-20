print(f'\nConversor from Roman number to arabic numbers')
s = input("\n\nInput a Roman number: \n")

romanNumber = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "C" : 100,
    "M" : 1000,
}


def converter(dict, s):
    lista = []
    for char in s:
        print(dict[char])
        lista.append(dict[char])
    return lista

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
        print(f"La suma en la iteración es: {sum}")

    print(lista)    
    return sum

            


lista = converter(romanNumber, s)
suma = calcNum(lista)




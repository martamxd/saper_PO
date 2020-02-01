import random
import time
import copy


#Macierz poczatkowa
b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Places a bomb in a random location.
def placeBomb(b):
    r = random.randint(0,8) #3
    c = random.randint(0,8) #8
   #Checks if there's a bomb in the randomly generated location.
   #If not, it puts one there. If there is, it requests a new location to try.
    currentRow = b[r]   #wyswietla r czyli 3 element listy b [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if not currentRow[c] == '*': #jesli element c w wierszu r nie jest * to wstaw * else random nowe r i c
        currentRow[c] = '*'
    else:
        placeBomb(b)

for i in range(0,10):
    placeBomb(b)

#Gets the value of a coordinate on the grid.
def loc(r,c,b):
    return b[r][c]

def updateValues(rn,c,b):

    #row above
    if rn-1 > -1: #musi byc ten warunek bo sprawdza czy jest jakies row above
        r = b[rn-1]

        if c-1 > -1: # tyllko jesli numer columny -1 czyli columna poprzednia jest wieksza od -1 czyli jest 0 czyli pierwsza col
            if not r[c-1] == '*': #jesli nie jest *
                r[c-1] += 1  #to dodaj do wierza tej kolumny wartosc 1
        
        if not r[c] == '*': #jesli columna dla wiersza obecnego nie jest *
            r[c] +=1 #dodajemy 1
        
        if c + 1 <9: #columna nasza plus 1 musi byc mniejsze od 9 bo mamy tylko 8 [0-8]
            if not r[c+1] == '*': #jesli wiersz w tej kolumnie nie jest '*'
                r[c+1] +=1 #dodajemy 1

    #same row
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1
    
    if c + 1 < 9:
        if not r[c+1] =='*':
            r[c+1] +=1

    #row below
    if rn+1 < 9:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] =='*':
                r[c-1] +=1
        
        if not r[c] == '*':
            r[c] +=1
        
        if c+1 < 9:
            if not r[c+1] == "*":
                r[c+1] +=1

for r in range (0,9):
    for c in range(0,9):
        value = loc(r,c,b)
        if value == '*':
            updateValues(r,c,b)

#Prints the given board.
def printBoard(b):
    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 9):
        print(r,'║' ,loc(r,0,b),'║',loc(r,1,b),'║',loc(r,2,b),'║',loc(r,3,b),'║',loc(r,4,b),'║',loc(r,5,b),'║',loc(r,6,b),'║',loc(r,7,b),'║',loc(r,8,b),'║')
        if not r == 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')


printBoard(b)
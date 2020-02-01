import random
import copy

def reset():
    #Macierz poczatkowa
    b = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    for i in range(0,5):
        placeBomb(b)

    for r in range (0,6):
        for c in range(0,6):
            value = loc(r,c,b)
            if value == '*':
                updateValues(r,c,b)

    #Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
    k = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ']]

    printBoard(k)

    play(b,k)

#Gets the value of a coordinate on the grid.
def loc(r,c,b):
    return b[r][c]

#Places a bomb in a random location.
def placeBomb(b):
    r = random.randint(0,5) 
    c = random.randint(0,5) 
   #Checks if there's a bomb in the randomly generated location.
   #If not, it puts one there. If there is, it requests a new location to try.
    currentRow = b[r]   #wyswietla r czyli 3 element listy b [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if not currentRow[c] == '*': #jesli element c w wierszu r nie jest * to wstaw * else random nowe r i c
        currentRow[c] = '*'
    else:
        placeBomb(b)

#Adds 1 to all of the squares around a bomb.        
def updateValues(rn,c,b):

    #row above
    if rn-1 > -1: #musi byc ten warunek bo sprawdza czy jest jakies row above
        r = b[rn-1]

        if c-1 > -1: # tyllko jesli numer columny -1 czyli columna poprzednia jest wieksza od -1 czyli jest 0 czyli pierwsza col
            if not r[c-1] == '*': #jesli nie jest *
                r[c-1] += 1  #to dodaj do wierza tej kolumny wartosc 1
        
        if not r[c] == '*': #jesli columna dla wiersza obecnego nie jest *
            r[c] +=1 #dodajemy 1
        
        if c + 1 <6: #columna nasza plus 1 musi byc mniejsze od 9 bo mamy tylko 8 [0-8]
            if not r[c+1] == '*': #jesli wiersz w tej kolumnie nie jest '*'
                r[c+1] +=1 #dodajemy 1

    #same row
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1
    
    if c + 1 < 6:
        if not r[c+1] =='*':
            r[c+1] +=1

    #row below
    if rn+1 < 6:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] =='*':
                r[c-1] +=1
        
        if not r[c] == '*':
            r[c] +=1
        
        if c+1 < 6:
            if not r[c+1] == "*":
                r[c+1] +=1

def zeroProcedure(r, c, k, b):

    #Row above
    if r-1 > -1:
        row = k[r-1]
        if c-1 > -1: row[c-1] = loc(r-1, c-1, b)
        row[c] = loc(r-1, c, b)
        if c+1 < 6: row[c+1] = loc(r-1, c+1, b)

    #Same row
    row = k[r]
    if c-1 > -1: row[c-1] = loc(r, c-1, b)
    if c+1<6: row[c+1] = loc(r, c+1, b)

    #Row below
    if 6 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = loc(r+1, c-1, b)
        row[c] = loc(r+1, c, b)
        if c+1 < 6: row[c+1] = loc(r+1, c+1, b)

#Checks known grid for 0s.
def checkZeros(k, b, r, c):
    oldGrid = copy.deepcopy(k)
    zeroProcedure(r, c, k, b)
    if oldGrid == k:
        return
    while True:
        oldGrid = copy.deepcopy(k)
        for x in range (6):
            for y in range (6):
                if loc(x, y, k) == 0:
                    zeroProcedure(x, y, k, b)
        if oldGrid == k:
            return

#Prints the given board.
def printBoard(b):
    print('    A   B   C   D   E   F ')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 6):
        print(r,'║' ,loc(r,0,b),'║',loc(r,1,b),'║',loc(r,2,b),'║',loc(r,3,b),'║',loc(r,4,b),
        '║',loc(r,5,b),'║')
        if not r == 5:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╝')

#The player chooses a location.
def choose(b,k):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    numbers = ['0', '1', '2', '3', '4', '5']
    while True:
        chosen = input('Wybierz nr kolumny i wiersza (np.B3): ').lower()
        if len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
    else: choose(b,k)

#The majority of the gameplay happens here.
def play(b,k):
    c,r = choose(b,k)
    v =loc(r,c,b)
    if v == '*':
        printBoard(b)
        print("You lose:(")
        quit()
    k[r][c] = v
    #Runs checkZeros() if that value is a 0.
    if v == 0:
        checkZeros(k, b, r, c)
    printBoard(k)
    #Checks to see if you have won.
    squaresLeft = 0
    for x in range (0, 6):
        row = k[x]
        squaresLeft += row.count(' ')
    if squaresLeft ==5:
        printBoard(b)
        print("You won :)")
        quit()
    play(b,k)
    
reset()
    

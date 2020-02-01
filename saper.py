import random
import copy

def reset():
    #Macierz do gry 6x6
    m = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    for i in range(0,5):
        placeBomb(m)

    for r in range (0,6):
        for c in range(0,6):
            value = loc(r,c,m)
            if value == '*':
                updateValues(r,c,m)

    #Macierz jest pusta 
    k = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ']]

    printBoard(k)

    play(m,k)

#lokalizacja
def loc(r,c,m):
    return m[r][c]

#polozenie bomby
def placeBomb(m):
    r = random.randint(0,5) 
    c = random.randint(0,5) 
   
    currentRow = m[r]   #wyswietla r element listy m [0, 0, 0, 0, 0, 0]
    if not currentRow[c] == '*': #jesli element c w wierszu r nie jest * to wstaw * else random nowe r i c
        currentRow[c] = '*'
    else:
        placeBomb(m)

#Dodaje wartosci w zaleznosci czy jest bomba wokół       
def updateValues(rn,c,m):

    #wierz obecny -1
    if rn-1 > -1: #musi byc ten warunek bo sprawdza czy jest jakies row above
        r = m[rn-1]

        if c-1 > -1: # tyllko jesli numer columny -1 czyli columna poprzednia jest wieksza od -1 czyli jest 0 czyli pierwsza col
            if not r[c-1] == '*': #jesli nie jest *
                r[c-1] += 1  #to dodaj do wierza tej kolumny wartosc 1
        
        if not r[c] == '*': #jesli columna dla wiersza obecnego nie jest *
            r[c] +=1 #dodajemy 1
        
        if c + 1 <6: #columna nasza plus 1 musi byc mniejsze od 6 bo mamy tylko 5 [0-5]
            if not r[c+1] == '*': #jesli wiersz w tej kolumnie nie jest '*'
                r[c+1] +=1 #dodajemy 1

    #obecny wiersz
    r = m[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1
    
    if c + 1 < 6:
        if not r[c+1] =='*':
            r[c+1] +=1

    #wiersz powyzej
    if rn+1 < 6:
        r = m[rn+1]

        if c-1 > -1:
            if not r[c-1] =='*':
                r[c-1] +=1
        
        if not r[c] == '*':
            r[c] +=1
        
        if c+1 < 6:
            if not r[c+1] == "*":
                r[c+1] +=1

def zeroProcedure(r, c, k, m):

    #wiersz nizej
    if r-1 > -1:
        row = k[r-1]
        if c-1 > -1: row[c-1] = loc(r-1, c-1, m)
        row[c] = loc(r-1, c, m)
        if c+1 < 6: row[c+1] = loc(r-1, c+1, m)

    #obecny wiersz
    row = k[r]
    if c-1 > -1: row[c-1] = loc(r, c-1, m)
    if c+1<6: row[c+1] = loc(r, c+1, m)

    #wiersz wyzej 
    if 6 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = loc(r+1, c-1, m)
        row[c] = loc(r+1, c, m)
        if c+1 < 6: row[c+1] = loc(r+1, c+1, m)

def checkZeros(k, m, r, c):
    oldGrid = copy.deepcopy(k)
    zeroProcedure(r, c, k, m)
    if oldGrid == k:
        return
    while True:
        oldGrid = copy.deepcopy(k)
        for x in range (6):
            for y in range (6):
                if loc(x, y, k) == 0:
                    zeroProcedure(x, y, k, m)
        if oldGrid == k:
            return


def printBoard(m):
    print('    A   B   C   D   E   F ')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 6):
        print(r,'║' ,loc(r,0,m),'║',loc(r,1,m),'║',loc(r,2,m),'║',loc(r,3,m),'║',loc(r,4,m),
        '║',loc(r,5,m),'║')
        if not r == 5:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╝')


def choose(m,k):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    numbers = ['0', '1', '2', '3', '4', '5']
    while True:
        chosen = input('Wybierz nr kolumny i wiersza (np.B3): ').lower()
        if len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
    else: choose(m,k)


def play(m,k):
    c,r = choose(m,k)
    v =loc(r,c,m)
    if v == '*':
        printBoard(m)
        print("You lose:(")
        quit()
    k[r][c] = v
  
    if v == 0:
        checkZeros(k, m, r, c)
    printBoard(k)
  
    squaresLeft = 0
    for x in range (0, 6):
        row = k[x]
        squaresLeft += row.count(' ')
    if squaresLeft ==5:
        printBoard(m)
        print("You won :)")
        quit()
    play(m,k)
    
reset()
    

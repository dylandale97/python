#opgave 1

#a
tup1 = (1, 2, 3, 4, 5)
tup2 = (5,)
print(tup1, tup2, sep="\n")

#b
tup = ('xx', 'yy', 'zz')
print(tup[1])

#c
tup1 = (4, 6, 2, 8, 3, 1)
tup1 = (4, 6, 100, 2, 8, 3, 1)
print(tup1)

#d
str = ""
tup = ('a', 'b', 'c')
for i in tup:
    str += i
print(str)

#e
L = [5, 10, 7]
L1 = tuple(L)
print(L1)
#f
L = [(1, 2), (3, 4), (8, 9)]
L1 = []

L1 = []
L2 = []
list_number = 0
for i in L:
    for y in i:
        if list_number == 0:
            list_number = 1
            print(list_number)
            L1.append(y)

        elif list_number == 1:
            list_number = 0
            L2.append(y)
print(L1)
# t = [1,2,3,4,5,6]
# print(t[::2])

# L1 = L[0] + (L[2][0],)
# L2 = L[::-2]

#g
L = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("y", 3), ("z", 4) ]
# D = "{ 'x': [1, 2, 3], 'y': [1, 2,3], 'z': [1] }"
List = {}
Tmp = []
keyword = ""
firstRun = True
for i in L:
    if firstRun == True:
        firstRun = False
        keyword = i[0]
    if keyword == i[0]:
        Tmp.append(i[1])
        keyword = i[0]
        List[keyword] = Tmp
    else:
        Tmp = []
        Tmp.append(i[1])
        keyword = i[0]
        List[keyword] = Tmp

print(List)

#opgave 2
d = {"red": 4, "blue": 4, "green": 14, "yellow": 2}

# a) De waarde van rood veranderd in blauw 4 wordt 1 {'red': 1, 'blue': 1, 'green': 14, 'yellow': 2}
a = d['red'] = d['blue']
# b) verandert de waarde van blauw door er een aantal bij op te tellen
d['blue'] += 10
# c) verandert geel in de lengte van de hashmap
c = d['yellow'] = len(d)
# d) verandert groen in een hashmap met daarin de waarde van orange : 6
d = d['green'] = {'orange' : 6}
# e) reset/verandert alle waarden in de lijst naar 0
e = d = dict.fromkeys(d, 0)
# f) verwijdert een element uit de lijst
f = d.pop('black', None)
# g) Haalt de waarde van black op
g = d.get('black', None)
# h) stuurt de waarde van de hash terug als deze bestaat, als de hash niet bestaat wordt er een nieuwe hash element aangemaakt met daarin de waarde
h = d.setdefault('black', None)
# i) maakt de lijst leeg/ stelt het opnieuw in
i = d = {}

#opgave 3

#a)
for item in sorted(D):
    print(item[0], item[1])


#b)
D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5}
D1 = {}
D2 = {}

for item in D:
    D1.setdefault(item, 0)
    for item2 in D:
        if D.get(item) == D.get(item2):
            D1[item] += 1
               

for item in D1:
    if(D1.get(item) == 1):
        for item2 in D:
            D2[item] = D.get(item)
        

print(D2)

#optie 2

from collections import Counter

D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5}
D1 = Counter(dict(D).values())
D2 = {}

for i in D:
    if D1[D.get(i)] == 1:
        D2[i] = D.get(i)

print(D2)

#c) toevoegen in een hashmap zonder key?

from collections import Counter

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
L1 = []
L2 = set()

for i in L:
    L1.append(list(dict(i).values())[0])

for y in Counter(L1):
    L2.add(y)

print(L2)

#d)
print(Counter(L[0]) + Counter(L[1]))


#e)
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

ind = dict(zip(keys, values))

print(ind)


#Opgave 4

#a) ID

#b)
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7} 
s3 = set()

# r = {3, 4, 5, 7}
equal = False
for x in s1:
    if equal == True:
        equal = False
    for y in s2:
        if(x == y):
            equal = True
    if equal == False:
        s3.add(x) 
for x in s2:
    if equal == True:
        equal = False
    for y in s1:
        if(x == y):
            equal = True
    if equal == False:
        s3.add(x) 

print(s3) 

#c)
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
L2 = [15, 11]
def findNumberInList(lst1, lst2) :
    Lst3 = []
    for itm in lst2:
        for itm2 in lst1:
            if itm == itm2:
                Lst3.append(itm)
    if(len(Lst3) == len(lst2)):
        return True
    else :
        return False

print(findNumberInList(L, L2))

#opgave 5

#a)
def capitalize_all(t):
    res = [s.capitalize() for s in t]  
    return res

print(capitalize_all("hallo"))

#b)

def only_upper(t):
    res = [s for s in t if s.isupper()]
    return res

print(only_upper("HalLo"))


#opgave 6

import string
from collections import Counter
L = [1, 2, 3, 3, 3, 3, 4, 5]
print(Counter(L).keys())
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in L1:
    if num % 2 == 0:
        print(num, end= " ")

unique = string.ascii_lowercase
unique1 = 'Hallo allemaal'
stringcount = len(unique)
if stringcount > 25:
    boolean = True
else:
    boolean = False
print(boolean)

dict = {'ed': 5, 'carl': 3, 'alan': 1, 'bob': 2, 'dan': 4}
print(sorted(dict.items()))

#opgave 7

#De main importeert mod b en c. In module b wordt module c al aangeroepen en in de main wordt ook module c aangeroepen dus er wordt 2 keer dezelfde klasse aangeroepen.

#opgave 8

from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4

# initializing board
board = []

for x in range(BOARD_SIZE):
 board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

# start the game and printing the board
print("Let's play Battleship!")
print_board(board)

# define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)


guessL = []
won = 0

while NR_GUESSES > 0:
    tempL = [0,0]

    print('Make a guess: ')
    print('Wich row?: ')
    guessrow = int(input())
    print('Wich place?: ')
    guessplace = int(input())

    for x in guessL:
        while x[0] == guessrow and x[1] == guessplace:
            print('This value is already chosen')
            print('Wich row?: ')
            guessrow = int(input())
            print('Wich place?: ')
            guessplace = int(input())
    while guessplace<=0 or guessrow<=0 or guessplace>4 or guessrow>4:
        print('Pick a value between 0 and 4')
        print('Wich row?: ')
        guessrow = int(input())
        print('Wich place?: ')
        guessplace = int(input())

    tempL[0] = guessrow
    tempL[1] = guessplace


    if guessrow == ship_row and guessplace == ship_col:
        print('You won!')
        won = 1
        break

    for x in range(BOARD_SIZE):
        if x+1 == guessrow:
            temp = board[guessrow-1]
            temp[guessplace-1] = 'x'

    print_board(board)


    guessL.append(tempL)

    NR_GUESSES = NR_GUESSES -1



if won == 0:
    print ("Game Over")


#opgave 9

getal = 28
Lsum = []
x = 0

while x < 10000:
    Ltemp = []
    sum = 0
    y = 2
    if y <= x:
        while y <= x:
            if x % y == 0:
                Ltemp.append(x/y)
            y = y+1
        for a in Ltemp:
            sum = sum + a
        if sum == x:
            Lsum.append(int(sum))
    x = x+1

print(Lsum)

#opgave 10


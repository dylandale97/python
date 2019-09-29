import time

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
str = "";
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

time.sleep(500)
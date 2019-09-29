#opgave 1

#a)
L = [1, 2, 3]
#b)
L = ['red', 'green', 'blue']
#c)
L = range(3, 4, 5)
#d)
L = ['a', 'b', 'c', 'd']

#opgave 2
L = [30, 1, 2, 1, 0, "hello", "Goodbye"]

#a) geeft de positie van 30 aan = 0
L.index(30)
#b) telt hoevaak 1 voorkomt in de lijst = 2
L.count(1)
#c) telt de lengte van de lijst = 7
len(L)
#d) geeft de maximale waarde weer; het moet wel een getal zijn
max(L)
#e) voegt een waarde toe aan de lijst
L.append(40)
#f) voegt een waarde in de lijst op een bepaalde plek
L.insert(2, 50)
#g) verlengt de lijst met een andere lijst
L.extend([1, 43])
#h verwijdert een waarde uit de lijst
L.remove("hello")
#i) ?????
L.pop()
#j) controleert of er een waarde in de lijst zit
"Goodbye" in L
#k) verwijdert een element uit een lijst
L.pop(0)
#l) sorteert de lijst op volgorde, het is nodig een range te gebruiken
L.sort()
#m) Gooit de elementen in de lijst door elkaar
random.shuffle(L)


#opgave 3
L = ['a', 'b', 'c', 'd', 'e']

#a) ['b'] Er is een begin en eindpositie opgegeven, het begin start bij 1 en het eind start bij de laatste - 3
L[1 : -3]
#b) geeft het resultaat ['b', 'c'] Beginpositie -4 en de eindpositie -2
L[-4 : -2]
#c) ['a', 'b', 'c'] geeft de eerste 3 in de lijst weer
L[:3]
#d) ['a', 'b', 'c', 'd', 'e'] geeft eerst de eerste 2 weer daarna begint de index bij 2 en wordt dat erbij opgetelt
L[:2] + L[2:]
#e) ['a', 'b', 'c', 'd'] geeft alleen de laatse niet weer
L[:-1]
#f) ['e', 'd', 'c', 'b', 'a'] geeft alles achterste voren weer, kan ook gebruikt worden om een aantal iets weer te geven door wat over te slaan
L[::-1]
#g) ['a', 'b', 'c', 'd', 'e']
L[:]

#opgave 4
L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]

#a) [30, 1, 2, 1, 0, 1, 21, 13] voegt de twee lijsten samen
L1 + L2
#b) [1, 21, 13, 1, 21, 13, 1, 21, 13] vermenigvuldigt de lijst van L2 3x
3 * L2
#c) True Kijkt of L1 groter is dan L2
L1 > L2
#d) [30, 1, 2, 1, 0] Zet de items over van L1
[x for x in L1]
#e) [1, 1] maakt een lijst door te kijken of de waarde van x ook voorkomt in L2
[x for x in L1 if x in L2]

#opgave 5
S = 'Guido van Rossum'
L = [x for x in S.split(' ')]

#opgave 6
#a)
L = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
 L[i] = L[i - 1]
 print(L)

# ------------------
# [1, 1, 3, 4, 5, 6]
# [1, 1, 1, 4, 5, 6]
# [1, 1, 1, 1, 5, 6]
# [1, 1, 1, 1, 1, 6]
# [1, 1, 1, 1, 1, 1]


#b)
L1 = list(range(1, 10, 2))
L2 = L1
L1[0] = 'abc'
print(L1)
print(L2)

# -------------------
# ['abc', 3, 5, 7, 9]
# ['abc', 3, 5, 7, 9]

#c)
a, b = 0, 1
while b < 10:
 print (b)
 a, b = b, a+b

#--
# 1
# 1
# 2
# 3
# 5
# 8

#opgave 7
def palindroom(w1):
    if w1 == w1[::-1]:
        return True
    else:
        return False

print(palindroom("lepel"))

#opgave 8 ID

#opgave 9

#a)

#b)
str = "AATGCCCTGA"
for i in range(len(str)):
    if str[i: i + 3] == "ATG":
        if str[i + 6: i + 9] in ["TAG", "TAA", "TGA"]:
            print(str[i + 3: i + 6])

#opgave 10
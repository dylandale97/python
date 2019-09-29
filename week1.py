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


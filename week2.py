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
L = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("y", 3) ]
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

print(List)

#opgave 2



time.sleep(500)
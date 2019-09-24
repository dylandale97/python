import time

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
# print(len(L))

# triples = []

L1 = []
L2 = []
list_number = 0
for i in L:
    for y in i:
        if list_number == 0:
            list_number = 1
            print(list_number)
            # L1 += str(y)
            L1.append(y)

        elif list_number == 1:
            list_number = 0
            L2.append(y)

            # L2 += str(y)

# L1 = [x for (x, y) in L]
# L2 = [y for (x, y) in L]

print(L1)


# t = [1,2,3,4,5,6]
# print(t[::2])

# L1 = L[0] + (L[2][0],)
# L2 = L[::-2]





time.sleep(500)
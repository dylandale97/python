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
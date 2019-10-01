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
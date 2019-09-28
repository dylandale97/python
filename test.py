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

for item in s2:
    for itm in s3:
        if

print(s3)    

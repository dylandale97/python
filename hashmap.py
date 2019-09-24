import time

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

time.sleep(5000)
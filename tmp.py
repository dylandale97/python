import time
import operator

D = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
Tmp = {}
Tmp_ltr = ""

# Tmp["test"] = "hallo"

for item in D:
    for item2 in D:

        if item2 < item:
            Tmp_ltr = item2
            Tmp[item2] = item2[0]



# for item in D:
print(Tmp)



# for i in range(D):
#     print(i)

time.sleep(5000)
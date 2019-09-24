import time
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}

# a)
a = d['red'] = d['blue']
# b)
# b = d['blue'] += 10
# c)
c = d['yellow'] = len(d)
# d)
d = d['green'] = {'orange' : 6}
# e)
e = d = dict.fromkeys(d, 0)
# f)
f = d.pop('black', None)
# g)
g = d.get('black', None)
# h)
h = d.setdefault('black', None)
# i)
i = d = {}

# print(a)
print(a, c, d, e, f, g, h, i, sep="\n")
time.sleep(5000)
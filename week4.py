#opdracht 4

#opdracht 5
from collections import namedtuple

Node = namedtuple('Node', 'data, left, right')

tree = Node(1, 
            Node(2, Node(4, Node(7, None, None), None),
                Node(5, None, None)),
            Node(3, Node(6, Node(8, None, None), 
                Node(9, None, None)),None))

def preorder(node):
    lst = []
    for item in node:
        try:
            if item.data:
                lst.append(int(item.data))
            if item.left.data:
                lst.append(int(item.left.data))
            if item.right.data:
                lst.append(int(item.right.data))
            # lst.append(int(item))         
        except:
            print()
            
    print(sorted(lst))

preorder(tree)

#optie 2

Node = namedtuple('Node', 'data, left, right')

tree = Node(1, 
            Node(2, Node(4, Node(7, None, None), None),
                Node(5, None, None)),
            Node(3, Node(6, Node(8, None, None), 
                Node(9, None, None)),None))

def preorder(node):
    print(node[0])

    if node[1] != None:
        preorder(node[1])
    
    if node[2] != None:
        preorder(node[2])


#opdracht 6



#opdracht 7
#a)
students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke", 4: "Teake", 5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"}
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
two_demensional_lst = []
tmp = []

for student in students:   
    for friendship in friendships:
        if friendship[0] == student or friendship[1] == student:
            if friendship[0] != student:
                tmp.append(friendship[0])
            else:
                tmp.append(friendship[1])
    two_demensional_lst.append(tmp)
    tmp = []
print(two_demensional_lst)

#b)
lst = []
tmp = ()

for student in students:
    tmp += (student, len(two_demensional_lst[student]))
    lst.append(tmp)
    tmp = ()

print(lst)

#c)

#d)
interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),(0, "Spark"), (0, "Storm"), (0, "Cassandra"),(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),(3, "statistics"), (3, "regression"), (3, "probability"), (4, "machine learning"), (4, "regression"), (4, "decision trees"),(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),(5, "Haskell"), (5, "programming languages"), (6, "statistics"),(6, "probability"), (6, "mathematics"), (6, "theory"), (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),(9, "Java"), (9, "MapReduce"), (9, "Big Data")]

# d = {key: value for (key, value) in interests}

d = {}
for key, value in interests:
    d.setdefault(key, list()).append(value) 

print(d)

#e)
d = {}
for key, value in interests:
    d.setdefault(value, list())

for key in d:
    for k, v in interests:
        if(v == key):
            d[key].append(k)
    
print(d)
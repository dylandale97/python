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





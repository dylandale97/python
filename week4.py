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
            lst.append(int(item))         
        except:
            print()
            
    print(sorted(lst))

preorder(tree)
#opdracht 6

#opdracht 7




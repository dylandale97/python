from collections import namedtuple

Node = namedtuple('Node','data, left, right')

tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))

def preorder(node):
    if node[0]: # value
        print(node[1])
    if node[1]: # links
        preorder(node[1])
    if node[2]: # rechts
        preorder(node[2])

def telop(n):
#    totaal = 0
#   for i in range(1,n+1):
#       totaal = totaal+i
    if n == 0:
        return 0
    return telop(n-1)+n
print(telop(10))
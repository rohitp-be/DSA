from BinaryTree import BinaryTree
from Node import Node
x = [10,4,23,3,6,25,22]
btree = BinaryTree()
for i in x:
    node = Node(i)
    btree.addNode(node)
    print("run - node added")
btree.displayTree()

btree.getBfs()

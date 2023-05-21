from LinkedList import SingleLinkedList
from Node import Node

print("enter number of nodes for linkedList")
n = int(input())
slList = SingleLinkedList()
for i in range(n):
    print("Enter Node to add: ")
    nodeValue = input()
    node = Node(nodeValue)
    slList.addNode(node)

slList.displayList()

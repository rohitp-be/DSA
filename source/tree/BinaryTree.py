import sys

sys.path.insert(0, '/home/rohit/Desktop/workspace/scripts/PS')
from Node import Node
from queue.Queue import Queue

class BinaryTree:
    rootNode = None
    
    def getRootNode(self):
        return self.rootNode
    
    def setRootNode(self, node):
        self.rootNode = node 

    def addNode(self, node):
        if self.rootNode is None:
            self.rootNode = node
        else:
            self.insertNode(self.rootNode, node)
        print("btree - node added")
                
    def insertNode(self, root, newNode):
        if root.value >= newNode.value:
            if root.left is None:
                root.left = newNode
            else:
                self.insertNode(root.left, newNode)
        else:
            if root.right is None:
                root.right = newNode
            else:
                self.insertNode(root.right, newNode)

    def displayTree(self):
        if self.rootNode is None:
            print("empty tree")
        else:
            self.printTree(self.rootNode)
    
    def printTree(self, node):
        if node is not None:
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)

    def getDfs(self):
        pass

    def getBfs(self) -> 'list':
        queue  = Queue()
        queue = self.buildqueue(self.rootNode, queue, queue.front)
        queue.display()  
        # return queue
    
    def buildqueue(self, node, queue, front) ->'list':
        queue.enqueue(node)
        if front == queue.rear:
            return queue
        else:
            front += 1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            self.buildqueue(queue[front], queue, front)
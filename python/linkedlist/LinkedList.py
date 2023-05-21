class SingleLinkedList():
    headNode = None
    def __init__(self):
        self.headNode = None

    def setRootNode(self, node):
        self.headNode = node
        print("Head node added")

    def getRootNode(self):
        return self.headNode

    def addNode(self, node):
        try:
            if self.headNode:
                temp = self.headNode
                while(temp.next):
                    temp = temp.next
                temp.next = node
                print("node added at the end")
            else:
                self.headNode = node
                print("Head node added")
        except Exception as ex:
            print("exception found ", ex)
    
    def delNode(self, node):
        pass

    
    def displayList(self):
        headNode = self.headNode
        while(headNode.next):
            print(headNode.value)
            headNode =  headNode.next
        print(headNode.value)

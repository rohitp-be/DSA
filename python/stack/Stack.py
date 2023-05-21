class Stack:
    def __init__(self):
        self.st = []
    def pop(self):
        return self.st.pop()
    def push(self, num):
        self.st.append(num)
    def isEmpty(self):
        if len(self.st) > 0:
            return False
        else:
            return True
    def toString(self):
        return str(self.st)
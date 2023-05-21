
class Queue:

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        try:
            self.queue.append(value)
            if(len(self.queue)<=1):
                self.front += 1
                self.rear += 1 
            else:
                self.rear +=1
            return True
        except:
            return False

    def dequeue(self):
        if (len(self.queue)<1):
            return False
        else:
            x = self.queue[self.front]
            self.front += 1
            return x
        
    def display(self):
        x = self.front
        while self.front <= self.rear:
            print(self.queue[self.front])
            self.front += 1

        self.front = x

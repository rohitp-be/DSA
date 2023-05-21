from PS.queue.Queue import Queue

qu = Queue()

for i in range(1, 6):
    qu.enqueue(i*i)

qu.display()
print("#"*25)
print(qu.dequeue())
print(qu.dequeue())
print("#"*25)
qu.display()
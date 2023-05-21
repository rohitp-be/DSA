import itertools 
counter= itertools.count(1)
def printMatrix(a):
    n = len(a)
    m = 0
    if n > 0:
        m = len(a[0]) 
    count = 0
    row = 0
    for i in range(n*m):
        print(a[row][count])
        if count == m-1:
           row += 1
           count = 0 
        elif count < m:
            count += 1

a=[[next(counter) for x in range(1,5)] for y in range(1,4)] 
printMatrix(a)

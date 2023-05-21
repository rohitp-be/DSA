"""
You are given n straight lines. You have to find a maximum number of points of intersection with these n lines.

Input : n = 4 
Output : 6

Input : n = 2
Output :1
"""

def numIntersect(n):
    if n==1:
        return 0
    else:
        return n*(n-1)//2
    
print(numIntersect(10))
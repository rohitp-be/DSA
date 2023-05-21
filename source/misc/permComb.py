from itertools import permutations, combinations

def getPerm(a, n):
    perm = permutations(a, n)
    return perm

def getComb(a, n):
    return combinations(a, n)

a = [1,2,3]
n = 2

print("combinations")
comb = (getComb(a, n))
for i in comb:
    print(i)
print("#"*20)
print("permutations")
perm = getPerm(a,n)
for i in perm:
    print(i)
print("#"*20)
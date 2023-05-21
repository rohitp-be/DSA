def knapsack(w, n):
    if n==0 or w==0:
        return 0
    
    if weight[n-1] > w:
        return knapsack(w, n-1)
    else:
        return max(value[n-1] + knapsack(w-weight[n-1], n-1), knapsack(w, n-1))


value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

x = knapsack(capacity,len(value))
print(x)
def getArray(arr)->'list':
    for i in range(len(arr)):
        if i!=0:
            arr[i] = arr[i] + arr[i-1]
    return arr

arr = [1,2,3,4,5]
print(getArray(arr))
def incermentLastDigit(nums)-> 'list':
    nums = [str(i) for i in nums]
    a= int("".join(nums))
    a += 1 
    nums = [int(i) for i in str(a)]
    return nums

def iterativeApp(nums)->list:
    out = [] 
    carry = 0
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            pass


nums = [9,9,9,9,9]
print(incermentLastDigit(nums))
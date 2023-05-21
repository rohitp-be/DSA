def twoSum(nums, target):
    map = {}
    out =[]

    for i in nums:
        if i in map.keys():
            out.append(map.get(i))
            out.append(nums.index(i))
            return out
        else:
            map[target-i] =  nums.index(i)
    return out

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
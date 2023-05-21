def firstMissingPositive(nums):
    nums = [item for item in nums if item > 0]
    nums1 = [0 for i in range(len(nums))]
    for i in nums:
        if i <= len(nums1):
            nums1[i-1] = 1
    for i in nums1:
        if i == 0:
            return (nums1.index(i)+1)
    return (len(nums1)+1)

nums = [3,4,-1,1]
print(firstMissingPositive(nums))
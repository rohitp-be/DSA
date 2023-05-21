def threeSum(nums):
    arraySum = set()
    negative = []
    positive = []
    isZero = False
    count = 0 
    for i in nums:
        if i == 0:
            isZero = True
        elif i < 0:
            negative.append(i)
        else:
            positive.append(i)
    if(len(negative)>0 and len(positive)==0) :
        return []
    if(len(positive)>0 and len(negative)==0) :
        return []
    if isZero:
        for i in negative:
            if (i*-1) in positive:
                triplet = (i, 0,  -1*i)
                arraySum.add(triplet)
    for i in range(len(positive)):
        for j in range(i+1, len(positive)):
            psum = -1 * (positive[i]+positive[j])
            if psum in negative:
                triplet = (positive[i], positive[j], psum)
                arraySum.add(triplet)
    for i in range(len(negative)):
        for j in range(i+1, len(negative)):
            psum = -1 * (negative[i]+negative[j])
            if psum in positive:
                triplet = (negative[i], negative[j], psum)
                arraySum.add(triplet)
    return list(arraySum)

# nums = [-1,0,1,2,-1,-4]
nums =[1,2,-2,-1]
print(threeSum(nums))
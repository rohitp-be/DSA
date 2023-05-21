
def jobScheduling(startTime, endTime, profit):
    jobTime = [endTime[i]-startTime[i] for i in range(len(startTime))]
    profitPerUnit = [profit[j]/jobTime[j] for j in range(len(jobTime))]
    maxProfit = 0
    coveredTime = []
    
    for i in range(len(profitPerUnit)):
        index = profitPerUnit.index(max(profitPerUnit))
        if len(coveredTime) == 0:
            maxProfit += profit[index]
            for j in range(startTime[index], endTime[index]):
                coveredTime.append(j)
        elif (startTime[index] < min(coveredTime) and endTime[index] < min(coveredTime)) or (startTime[index] > max(coveredTime) and endTime[index] > max(coveredTime)) :
            maxProfit += profit[index]
            for j in range(startTime[index], endTime[index]):
                coveredTime.append(j)
        profitPerUnit.pop(index)
        startTime.pop(index)
        endTime.pop(index)
        profit.pop(index)
    
    print("maximum profit : ", maxProfit)

    
def byRecursions(startTime, endTime, profit):
    maxProfit = 0
    for i in range(len(startTime)):
        coveredTime = []
        LocalProfit = 0
        if len(coveredTime) ==0 :
            pass


startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

# startTime = [1,1,1]
# endTime = [2,3,4]
# profit = [5,6,4]

jobScheduling(startTime, endTime, profit)
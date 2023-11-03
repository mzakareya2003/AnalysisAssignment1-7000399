"""
Mohamed Ihab Seifeldin Zakaria 
7000399 / T-2
"""
#2(a)
import time
import matplotlib.pyplot as plt
import random

def mergeSort(array):
    
    if len(array) > 1:
        
        midIndex = len(array)//2
        leftHalf = array[:midIndex]
        rightHalf = array[midIndex:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftIndex = 0 #left array's index
        rightIndex = 0 #right array's index
        i = 0 #index to guide the origin array 

        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                array[i] = leftHalf[leftIndex]
                leftIndex += 1
            else:
                array[i] = rightHalf[rightIndex]
                rightIndex += 1
            i += 1

        while leftIndex < len(leftHalf):
            array[i] = leftHalf[leftIndex]
            leftIndex += 1
            i += 1

        while rightIndex < len(rightHalf):
            array[i] = rightHalf[rightIndex]
            rightIndex += 1
            i += 1

def binarySearch(array, target):#assuming sorted array
    low = 0 
    high = len(array) - 1
    pairsArray = []

    while low < high:
        sum = array[low] + array[high]
        if sum == target:
            pairsArray.append((array[low], array[high]))
            low += 1
            high -= 1
        elif sum < target:
            low += 1
        else:
            high -= 1

    return pairsArray

def getPairsEqualsTarget(inputArray, target):
    mergeSort(inputArray) #sort the array then pass it to binarySearch
    pairs = binarySearch(inputArray, target) #binarySearch gets possible pairs with sum==target
    return pairs

def timeTaken(computingFunction, a, n):
    start_time = time.time()
    computingFunction(a, n)
    end_time = time.time()
    return (end_time - start_time)




nArray = list(range(1, 10000, 100))
pairsTimeArray = []
for n in nArray:
    S = [random.randint(0, n) for i in range(n)]
    pairsTimeTaken = timeTaken(getPairsEqualsTarget, S, n)
    pairsTimeArray.append(pairsTimeTaken)

    
plt.plot(nArray, pairsTimeArray, label='pairs that sum==s')
plt.xlabel('value of n')
plt.ylabel('time/seconds')
plt.legend()
plt.show()


#2(b)
# THEORETICALLY merge sort time complexity is o(nlog(n))
# AND binary search time complexity is O(log(n)) 
# BUT the modified binary search we created time 
# complexity is expected to be higher and possibly 
# equal to O(n)  so I will consider it O(n) theoritically
# therefore our program using both of these sequentially
# would prove time complexity of O(nlog(n))+O(n) which 
# AND the complexity is the dominant therefore it is theoretically O(nlog(n))


# 2(c) 
# The answer corresponds to our expected time complexity which is overall O(nlog(n))


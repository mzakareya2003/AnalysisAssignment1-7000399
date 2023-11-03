"""
Mohamed Ihab Seifeldin Zakaria 
7000399 / T-2
"""

#1(a)(i)

def naive(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result

print(naive(5,3))

#1(a)(ii)

def divideNconquer(a, n):
    if n==0:# trivial case or ending clause to recursion
        return 1
    elif (n%2)==0:# n is even
        half = divideNconquer(a, n//2)
        return half * half
    elif (n%2)!=0:# n is odd
        half = divideNconquer(a, (n-1)//2)
        return a * half * half

print(divideNconquer(5,3))

#1(b)
#the theoritically expected for the naive method would be O(n) and for the divide&conquer method would be o(log(n))

#1(c)
import time
import matplotlib.pyplot as plt

def divideNconquer(a, n):
    if n==0:# trivial case or ending clause to recursion
        return 1
    elif (n%2)==0:# n is even
        half = divideNconquer(a, n//2)
        return half * half
    elif (n%2)!=0:# n is odd
        half = divideNconquer(a, (n-1)//2)
        return a * half * half

def naive(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


def timeTaken(computingFunction, a, n):
    start_time = time.time()
    computingFunction(a, n)
    end_time = time.time()
    return (end_time - start_time)

nArray = list(range(1, 1000002, 100000))
naiveTimeArray = []
dNcTimeArray = []
for n in nArray:
    naiveTime = timeTaken(naive, 2, n)
    dNcTime = timeTaken(divideNconquer, 2, n)
    naiveTimeArray.append(naiveTime)
    dNcTimeArray.append(dNcTime)

    
plt.plot(nArray, naiveTimeArray, label='Naive Iterative')
plt.plot(nArray, dNcTimeArray, label='Divide and Conquer')
plt.xlabel('value of n')
plt.ylabel('time/seconds')
plt.legend()
plt.show()

1(d) 
#explained in the report


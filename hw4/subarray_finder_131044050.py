# Eda Arikan 131044050

# Worst case: O(n * Logn) 

import sys

index = []

def element(x):
    return x[0]


# Call from main, it returns minimum subarray   
def min_subarray_finder(inpArr):
    msa, index = minSubArrayWrapper(inpArr, 0, len(inpArr)-1)
    # print(index)
    return inpArr[index[0] : index[1] + 1]
    
    
# For left halves and right halves make recursive call       
def minSubArrayWrapper(array, left, right):
    mid = int((left+right)/2)
    global index
    
    if left == right: return (array[left], (left,right))
      
    return  min(minSubArrayWrapper(array, left, mid),
                minSubArrayWrapper(array, mid + 1, right),
                minSubArray(array, left, mid, right), 
                key = element)
 
 
# Calculate minimum sum for left and right halves
def minSubArray(array, left, mid, right):
    rightMin = leftMin = sys.maxsize
    rightSum = leftSum = 0
    
    for i in range(mid + 1, right + 1, 1):
        rightSum += array[i]
        if rightSum < rightMin: rightMin = rightSum; rightIndex = i
            
    for i in range(mid, left - 1, -1):
        leftSum += array[i]
        if leftSum < leftMin: leftMin = leftSum; leftIndex = i
        
    return rightMin + leftMin, (leftIndex, rightIndex)


# main
if __name__ == "__main__": 
    inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
    msa = min_subarray_finder(inpArr)
    print(msa)
    print(sum(msa))
    
    


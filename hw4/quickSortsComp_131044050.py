# Eda Arikan 131044050

# Swap two elements in the array
def swap(array, i, j):
    temp = array[i] 
    array[i] = array[j] 
    array[j] = temp
    

################################################################################    
# Lomuto’s partition 
    
# call from main
def quickSortLomuto(array):
    quicksortLomutoWrapper(array, 0 , len(arr) - 1)
    return array


# returns sorted array 
def quicksortLomutoWrapper(array, start, end):       
    if start < end:
        pivot_position = lomutoPartition(array, start, end)
        quicksortLomutoWrapper(array, start, pivot_position - 1)
        quicksortLomutoWrapper(array, pivot_position + 1, end)
    
    
# Lomuto partition
def lomutoPartition(array, start, end):
    swap_position = start - 1
    pivot = array[end]
        
    for i in range(start, end, 1):
        if array[i] <= pivot:
            swap_position += 1
            swap(array, swap_position, i)
    swap(array, swap_position + 1, end)
    
    return swap_position + 1
    
    
################################################################################    
# Hoare’s partition 

# call from main
def quickSortHoare(array):
    quicksortHoareWrapper(array, 0 , len(arr) - 1)
    return array


# Hoare partition
def hoarePartition(array, start, end):
    pivot = array[start]
    i = start - 1
    j = end + 1

    while(True):
        j -= 1
        while array[j] > pivot: j -= 1
        i += 1
        while array[i] < pivot: i += 1

        if j > i:  swap(array, i, j)
        else: return j


# returns sorted array 
def quicksortHoareWrapper(array, start, end):
    if start < end:
        pivot_position = hoarePartition(array, start, end)
        quicksortHoareWrapper(array, start, pivot_position)
        quicksortHoareWrapper(array, pivot_position + 1, end)


    
if __name__ == "__main__": 
    arr = [15, 4, 68, 24, 75, 16, 42, 5, 6, 4, 55, 88, 99, 1024, 555, 115]
    qsl = quickSortLomuto(arr)
    print(qsl)
    
    # hoareye gonderilen array yeniden tanimlanmali, 
    # cunku lomuto orjinal arrayi degistirdi.
    
    arr = [15, 4, 68, 24, 75, 16, 42, 5, 6, 55, 5, 88, 99, 555, 11, 99, 1024] 
    qsh = quickSortHoare(arr)
    print(qsh)
    
    

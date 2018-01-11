# Eda Arikan - 131044050

# It's time complexity is O(n)


# returns maximum cost
def find_maximum_cost(array):
    # array length
    length = len(array)
    
    # check length
    if array is None or length == 0: 
        return 0
    
    if length == 1:
        return 0
    else:        
        # For store to below two solution, create [length][2] dimension array
        store = [[0 for i in range(2)] for j in range(length)]
        
        for i in range(1, length):
            #First solution:  [i]th element is min and [i-1]th element is max or min
            store[i][0] =  max(abs(1 - array[i - 1]) + store[i - 1][1], store[i - 1][0])
            #Second solution: [i]th element is max and [i-1]th element is min or max
            store[i][1] =  max(abs(array[i] - 1) + store[i - 1][0], store[i - 1][1])

        # compare the last max values
        return(max(store[length - 1][0], store[length - 1][1]))


# main
if __name__ == "__main__":
    Y = [80, 22, 45, 11, 67, 67, 74, 91, 4, 35, 34, 65, 80, 21, 95, 1, 52, 25, 31, 2, 53]
    cost = find_maximum_cost(Y)
    print(cost)
    
    Y = [14, 1, 14, 1, 14]
    cost = find_maximum_cost(Y)
    print(cost)
    
    Y = [1, 9, 11, 7, 3]
    cost = find_maximum_cost(Y)
    print(cost)
    
    Y = [50, 28, 1, 1, 13, 7]
    cost = find_maximum_cost(Y)
    print(cost)
        
    Y = [79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91]
    cost = find_maximum_cost(Y)
    print(cost)

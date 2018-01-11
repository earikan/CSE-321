# Eda Arikan - 131044050

# It's time complexity depends on input's size.
# So the complexity is O(row * column)


# return inputs size
def findRowAndColumn(array):
    max_size_row = len(array) 
    max_size_col = len(array[0]) 
 
    return max_size_row, max_size_col
   
    
# return max money that thief can steal   
def theft(moneyArray):
    # get size
    max_size_row, max_size_col = findRowAndColumn(moneyArray)
    maxMoney = 0
    
    # if null, return 0
    if moneyArray is None or len(moneyArray) == 0: 
        return 0
        
    # create new array to store max money in each row how much money will he earn if he goes this way   
    maxMoneyArray = [[0]*max_size_col for i in range(max_size_row)]
    
    # copy it to original array
    maxMoneyArray = moneyArray
    
    for j in range(max_size_col - 2, -1, -1):
        for i in range(0, max_size_row):
            # if it is in first row, where is max money, he can only go right or right down
            if(i == 0 and i != max_size_row - 1):
                maxMoneyArray[i][j] = moneyArray[i][j] + max(maxMoneyArray[i][j+1], maxMoneyArray[i+1][j+1])
			# if it is in left corner, only go right
            elif(i == 0 and i == max_size_row - 1):
                maxMoneyArray[i][j] = moneyArray[i][j] + maxMoneyArray[i][j+1]
			# if it is in last row, where is max money, he can only go right or right up
            elif(i != 0 and i == max_size_row - 1):
                maxMoneyArray[i][j] = moneyArray[i][j] + max(maxMoneyArray[i][j+1], maxMoneyArray[i-1][j+1])
			# otherwise find max money way and go
            else:
                maxMoneyArray[i][j] = moneyArray[i][j] + max(maxMoneyArray[i-1][j+1], maxMoneyArray[i][j+1], maxMoneyArray[i+1][j+1])
	
	# return max money			
    for i in range(0, max_size_row):
        if maxMoney < maxMoneyArray[i][0]:
            maxMoney = maxMoneyArray[i][0]
	        
    return maxMoney        	
		

# main
if __name__ == "__main__":        
    amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
    res = theft(amountOfMoneyInLand)
    print(res)     
    
    amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
    res = theft(amountOfMoneyInLand)
    print(res)   

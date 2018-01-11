# 131044050
# brute force algorithm to find the optimal solution of minimizing
# the total time spent for course assistantship


# ONLY WORKS FOR n=r


# permutations all possible research assistant assignments as 1d array 
# returns [1,0,2,2,1,0,1,2,0..]   
def permutation(start, RA_array, permutation_array):

    if(start == len(RA_array)):
        permutation_array.extend(RA_array)  
        return
    
    for i in range(start,len(RA_array)):
        temp = RA_array[i]
        RA_array[i] = RA_array[start];
        RA_array[start] = temp;
        
        permutation(start + 1, RA_array, permutation_array);
        
        temp = RA_array[i]
        RA_array[i] = RA_array[start];
        RA_array[start] = temp;
        



# takes 1d array and converts to 2d array like [[1,0,2],[2,1,0],[1,2,0]..]       
def reshapeArray_1d_to_nd(permutation_array, RA_array_length):

    temp = []
    index = 0
    for i in range(int(len(permutation_array)/RA_array_length)):
        temp.append([])
        for j in range(index, index+RA_array_length):
            temp[i].append(permutation_array[j])   
        index = index + RA_array_length
    return temp
        
 
 
 
# it returns [0, 1, 2] as research assistants       
def create_RA_Array(inputTable):

    RA_array = []
    for i in range(len(inputTable)):
        RA_array.append(i)
        
    return RA_array    
    



# finds optimum solution        
def findOptimalAssistantship(inputTable):

    permutation_array = []
    permutation(0, create_RA_Array(inputTable), permutation_array)
    permutation_array = reshapeArray_1d_to_nd(permutation_array, len(create_RA_Array(inputTable)))
    
    min_cost_array = []
    cost = 0
    
    for i in range(len(permutation_array)):
        k = 0
        for j in range(len(inputTable[0])):
            cost += inputTable[k][permutation_array[i][j]]
            k += 1
        min_cost_array.append(cost)
        cost = 0      
    
    index = min_cost_array.index(min(min_cost_array))
    
    return permutation_array[index], min(min_cost_array)




if __name__=='__main__':

    inputTable =  [[5, 8, 7], [8, 12, 7], [4, 8, 5]] 
    list_RA, min_cost = findOptimalAssistantship(inputTable)
    print(list_RA)
    print(min_cost) 


      

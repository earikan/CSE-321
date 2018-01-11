# Eda Arikan 131044050

# Worst case: O(k * Logn) 
# k: input size
# n: maximum length size string in input list
 
 
# returns reverse of a string
def reverseString(string):
    string = string[::-1]
    return string
    
    
# find minimum length between two strings
def min_length(firstStr, secondStr):
    if(len(firstStr) > len(secondStr)):
        return len(secondStr)
    else:
        return len(firstStr)    
        
        
# returns a list reverse with reverse each element        
def reverseList(inpStrings):
    output = []
    for i in inpStrings:
        output.append(reverseString(i))  
          
    return output


# solve minimum problem, between two strings   
def longest_common_postfix_micro(firstStr, secondStr):
    output = ""
    for i in range(0, min_length(firstStr, secondStr)):
        if(firstStr[i] == secondStr[i]):
            output += (firstStr[i])
            
    return output

    
# solve whole problem with recursive call
def longest_common_postfix_wrapper(start, end, stringList):
    if (start == end):
        return stringList[start]
    
    if(end > start):    
        mid = start + (end - start) // 2;            
        firstStr = longest_common_postfix_wrapper(start, mid, stringList);
        secondStr = longest_common_postfix_wrapper(mid + 1, end, stringList);    
        
        return (longest_common_postfix_micro(firstStr, secondStr));    
            

# call from main            
def longest_common_postfix(inpStrings):
    allReverseList = reverseList(inpStrings)
    output = longest_common_postfix_wrapper(0, len(allReverseList) - 1, allReverseList); 
    
    if(len(output) == 0): print("Not found longest common postfix.")
    else: return reverseString(output)
    
         
# main           
if __name__ == "__main__": 
    inpStrings = ["absorptivity", "abscularity", "absctricity", "absortunity", "absanity"]   
    lcp = longest_common_postfix(inpStrings);
    print(lcp) 
     
     
     

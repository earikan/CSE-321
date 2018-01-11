# Eda Arikan - 131044050

# It's time complexity is O(n)
# x*3 + y*5 = N 

# calculate decent number
def decentNumber(number):
    total_num_threes = 0
    total_num_fives = int(number)
    returnString = ""
    
    while total_num_fives % 3 != 0 or (total_num_fives >= 0 and total_num_threes % 5 != 0):
        total_num_fives -= 1
        total_num_threes += 1
        
    if total_num_fives < 0:
        return(-1)
    else:
        for i in range(total_num_fives):
            returnString += '5'
        for i in range(total_num_threes):
            returnString += '3'
        
        return returnString     
        
# main
if __name__ == "__main__":  
    dn = decentNumber(1)
    print(dn)
    
    dn = decentNumber(3)
    print(dn)
  
    dn = decentNumber(5)
    print(dn)
   
    dn = decentNumber(11)
    print(dn)
    

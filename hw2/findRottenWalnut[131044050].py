def compareScales(left,right):
    result = sum(left) - sum(right)
    if result < 0:    
        return 1
    elif result > 0:
        return -1
    else:
        return 0

def foo(array,start):
    mid = int(len(array)/2)
    if(len(array) == 2):
        if array[0] > array[1]:
            return start
        if array[0] < array[1]:
            return start+1
        
    if len(array) % 2 == 0:
        res = compareScales(array[0:mid], array[mid:] )
        if res == 1:
            return foo(array[0:mid],start)
        elif res == -1:
            return foo(array[mid:],start+mid)
    else:
        res = compareScales(array[0:mid], array[mid+1:] )
        #print(array[0:mid],"and", array[mid+1:], "and last",res)
        if res == 1:
            return foo(array[0:mid],start)
        elif res == -1:
            return foo(array[mid+1:], start+mid)
        else:
            return start+mid


if __name__ == "__main__":
    print(foo([1,1,1,1,1,1,1,1,0.5,1],0))

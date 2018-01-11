# eda arikan - 131044050

#save moving times in list
timeList = []

#create own stack class with list
class Stack:

    # Construct stack
    def __init__(self, namelist):
        self.name = namelist
        self.stack = list()
        
    # Add element to stack
    def push(self, data):
        self.stack.append(data)
        return True

    # Remove element from the stack
    def pop(self):
        if len(self.stack) <= 0:
            return 'empty stack'
        return self.stack.pop()

    # Size of the stack
    def size(self):
        return len(self.stack)



# move disks
# s: source stack, a: auxiliary stack, d: destination stack, n: number of disks
def move_disks(n,s,a,d):

    if n == 0:
        d.push(s.pop())
        print ('disk',n + 1,':',s.name,'->',d.name)
        move_times(s, d, n)
    else:
        move_disks(n - 1, s, d, a)
        d.push(s.pop())
        print ('disk',n + 1,':',s.name,'->',d.name)
        move_times(s, d, n)
        move_disks(n - 1, a, s, d)



# elapsed time for each disk
# s: source stack, d: destination stack, n: number of disks
def move_times(s, d, n):

    if s.name == 'SRC' and d.name == 'DST' or s.name == 'DST' and d.name == 'SRC':
        timeList[n] += 2 * (n + 1)
    else:
        timeList[n] += n + 1



# initilaze hanoi
# n: number of disks
def hanoi(n):

    src = Stack('SRC')
    dest = Stack('DST')
    aux = Stack('AUX')
    i = n - 1
    while i >= 0:
        src.push(i)
        i -= 1
    move_disks(n - 1, src, aux, dest)



# main function
# n: number of disks
if __name__ == '__main__':

    n = 3
    timeList = [0] * n
    hanoi(n)
    print ('Elapsed time for disks:')
    print (timeList)


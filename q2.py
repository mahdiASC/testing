import copy
def answer(n):
    outcome = allPoss(n,n-1)
    return outcome

def allPoss(n,maximum):
    if n<=3:
        return 1
    
    output = 0
    for i in range(maximum,2,-1):
        leftover = n-i
        if i<=leftover:
            if validStair(leftover,i-1):
                output = output + allPoss(leftover,i-1)
        else:
            output=output+1
            if leftover>=3:
                output = output + allPoss(leftover,leftover-1)
    return output

def validStair(n,maximum):
    total = n
    for i in range(maximum,0,-1):
        total = total -i
    return total<=0

def createPattern(maximum=30):
    output = []
    for i in range(3,maximum):
        output.append(answer(i))
    
    return output
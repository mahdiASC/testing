
import copy
def answer(n):
    outcome = allPoss(n,n-1)
    print(outcome)
    if isinstance(outcome[0],int):
        return 1
    else:
        return len(outcome)

def allPoss(n,maximum):
    if n<=3:
        return [2,1]
    
    output = []
    for i in range(maximum,2,-1):
        leftover = n-i
        temp = [i,leftover]
        if i<=leftover:
            if validStair(leftover,i-1):
                tails = allPoss(leftover,i-1)
                conjoin(temp,tails,output)
        else:
            output.append(temp)
            if leftover>=3:
                tails = allPoss(leftover,leftover-1)
                conjoin(temp,tails,output)
    return output


def conjoin(list1,list2,target):
    if isinstance(list2[0],int):
        newTemp = copy.copy(list1)
        newTemp.pop()
        newTemp.extend([2,1])
        target.append(newTemp)
    else:
        for i in list2:
            newTemp = copy.copy(list1)
            newTemp.pop()
            newTemp.extend(i)
            target.append(newTemp)

def validStair(n,maximum):
    total = n
    for i in range(maximum,0,-1):
        total = total -i
    return total<=0
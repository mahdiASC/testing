import copy

def answer(n):
    outcome = {} #start 0 with 1

    for i in range(n+1):
        temp = copy.copy(outcome)
        if i<4:
            temp[i]=1
        if i>3:
            for k in outcome:
                if k+i <= n:
                    hashAdd(k+i, 1, temp)
            temp[i] = temp[i] + temp[i-4]
        
        outcome = temp
        print(outcome)
    return outcome
def hashAdd(key, val, hash):
    if key in hash:
        hash[key] = hash[key] + val
    else:
        hash[key] = 1
    
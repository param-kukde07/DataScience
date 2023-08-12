def checkIfNotNumeric(*args):
    for i in args:
        if not(isinstance(i,(int,float))):
            return False
    return True

def addAllNumeric(*args):
    s = 0
    for i in args:
        s+=i
    return s
def swapValues(L,idx1,idx2):
    temp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = temp
    return L
myName = "Python Course"
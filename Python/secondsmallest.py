import sys
arr=[-1,-2,-3,6,7,9,10,11]
def secondsmallest(arr):
    firstSmallest = secondsmallest = sys.maxsize
    for ele in arr:
        if(ele<firstSmallest):
            secondsmallest=firstSmallest
            firstSmallest=ele
        elif(ele<secondsmallest):
            secondsmallest= ele
    if(secondsmallest==sys.maxsize):
        return ("No second smallest")
    
    return secondsmallest
def secondLargest(arr):
    first = second = -sys.maxsize-1
    for ele in arr:
        if(ele>first):
            second = first
            first = ele
        elif(ele>second):
            second = ele
    if(second==-sys.maxsize-1):
        return("no second largets")
    return second
print(secondLargest(arr))
    
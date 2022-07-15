#0, -2, -1, -3, 4
def minstepsprod(a):
    zero,pos,neg=0,0,0
    count= 0
    for i in range(len(a)):
        if(a[i]==0):
            zero=zero+1
        elif(a[i]<0):
            count = count + (-1-(a[i]))
        else:
            count=count+(a[i]-1)
    if(neg%2==0):
        count = count + zero
    else:
        if(zero>0):
            count=count+zero
        else:
            count=count+2
    return count
    
a = [0, -2, -1, -3, 4]
print(minstepsprod(a))
    
# EVEN AND ODD PROBLEMS
def evenodd(a):
    even = 0
    odd=1
    n=len(a)
    while(True):
        
        while(even<n and a[even]%2==0):
            even = even+2
        while(odd<n and a[odd]%2==1):
            odd=odd+2
        if(even<n and odd<n):
            a[even],a[odd]=a[odd],a[even]
        else:
            break
    return a
        
a=[ 3, 6, 12, 1, 5, 8 ]
print(evenodd(a))
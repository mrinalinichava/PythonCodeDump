#REPLACE EACH ELEMENT WITH THE PRODUCT OF EVERY OTHER ELEMENT

#A=[1,2,3,4,5]

def rep_prod(a):
    n=len(a)
    left=[0]*n
    right=[0]*n
    left[0]=1
    right[n-1]=1
    for i in range(1,n):
        left[i]=a[i-1]*left[i-1]
    for j in range(n-2,-1,-1):
        right[j]=a[j+1]*right[j+1]
    for i in range(n):
        a[i]=left[i]*right[i]
    return a
a=[1,2,3,4,5]
print(rep_prod(a))

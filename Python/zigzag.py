a=[4,3,7,8,6,2,1]
n=len(a)
def zigzag(a):
    n=len(a)
    flag=1
    i=0
    while(i<n-1):
        if(flag==1 and a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
            i=i+1
            flag=0
        elif(flag==0 and a[i]<a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
            i=i+1
            flag=1
        else:
            i=i+1
            flag=flag^1
    return a
print(zigzag(a))


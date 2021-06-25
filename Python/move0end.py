#MOVE ALL THE ZEROS PRESENT IN AN ARRAY TO END
#[6,0,8,2,3,0,4,0,1]
#680230401
def moveend(a):
    n=len(a)
    i=0
    for i in range(n):
        if(a[i]==0):
            for j in range(i+1,n):
                #print(i)
                if(a[j]!=0):
                    a[i],a[j]=a[j],a[i]
                    i=j
    return a

a=[6,0,8,2,3,0,4,0,1]    
print(moveend(a))
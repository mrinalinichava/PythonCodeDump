#MOVE ALL THE ZEROS PRESENT IN AN ARRAY TO END
#[6,0,8,2,3,0,4,0,1]
#680230401
# def moveend(a):
#     n=len(a)
#     i=0
#     for i in range(n):
#         if(a[i]==0):
#             for j in range(i+1,n):
#                 #print(i)
#                 if(a[j]!=0):
#                     a[i],a[j]=a[j],a[i]
#                     i=j
#     return a

# a=[6,0,8,2,3,0,4,0,1]    
# print(moveend(a))

# efficient approach
def move(a):
    low = 0
    high = len(a)-1
    while(low<=high):
        if(low!=0):
            low=low+1
        
        if(a[high]==0):
            high=high-1
        elif(a[low]==0 and a[high]!=0):
            a[low],a[high]= a[high],a[low]
        elif(a[low]!=0):
            low=low+1
        else:
            low=low+1
            high = high -1
    return a
a=[6,0,8,2,3,0,4,0,1]    
print(move(a))
#SORT AND ARRAY 0's 1's
#[0,0,0,0, 1 ,1 ,1 ,0 , 0, 0,1,1,1,0 ]

def sortbin(a):
    n=len(a)
    i=0
    j=n-1
    while(i<j):
        if(a[i]==0 or a[j]==1):
            i=i+1
            j=j-1
        elif(a[i]==1 and a[j]==0):
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    #a[i],a[j]=a[j],a[i]
    return a
a=[1 ,0, 1, 1, 1, 1, 1, 0, 0, 0]
print(sortbin(a))

def sortBinaryArray (arr, n):
    # Your code here
    low=0
    high=n-1
    while(low<high):
        
        if(arr[low]==1):
            arr[high],arr[low]=arr[low],arr[high]
            high=high-1
        else:
            low=low+1
    return arr

#SORT AN ARRAY OF 0'S 1'S AND 2'S

# def sortarr(a):
#     low=0
#     mid=0
#     high=len(a)-1
#     while(mid<=high):
#         if(a[mid]==0):
#             a[low],a[mid]=a[mid],a[low]
#             low=low+1
#             mid=mid+1
#         elif(a[mid]==1):
#             mid=mid+1
#         else:
#             a[mid],a[high]=a[high],a[mid]
#             high=high-1
#     return a
# a=[0,1,1,2,0,2,1,1,0,0]
# print(sortarr(a))
        



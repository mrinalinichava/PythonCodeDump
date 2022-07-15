def seggregate(arr):
    low = 0
    high = len(arr)-1
    while(low<high):
        if(arr[low]==1):
            if(arr[high]==0):
                arr[low],arr[high]=arr[high],arr[low]
            else:
                high=high-1
        else:
            low=low+1
    return arr
arr=[1,0,1,0,1,1,1,1,0,1,0,0,0,0,0]
print(seggregate(arr))

### move neg to one end positive to another and zero in middle
arr=[2,-1,0,1,0,-3,-4,5]
def move(arr):
    n= len(arr)
    low,mid,high = 0,0,n-1
    while(mid<=high):
        if(arr[mid]==0):
            mid=mid+1
        elif(arr[mid]<0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif(arr[mid]>0):
            arr[mid],arr[high]=arr[high],arr[mid]
            high = high-1
        # print(arr)
    return arr
print(move(arr))
    
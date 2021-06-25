#Max length subarray with a given sum
from collections import defaultdict
def maxlensub(a,k):
    d=defaultdict(int)
    n=len(a)
    sumy=maxi=0
    for i in range(n):
        sumy=sumy+a[i]
        if(sumy-k in d):
            #print(i-d[sumy-k])
            maxi=max(maxi,i-d[sumy-k])
        elif(sumy==k):
            maxi=max(maxi,i)
        d[sumy]=i
    return maxi
a=[5,-6,-5,5,3,5,3,0,0]
k=8
print(maxlensub(a,k))


#trapping rain water
def trap(arr):
    n=len(arr)
    left =[0]*n
    right=[0]*n
    water = 0
    left[0]=arr[0]
    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i]= max(arr[i],right[i+1])
    for i in range(1,n):
        left[i]= max(arr[i],left[i-1])
    print(left)
    print(right)
    for i in range(n):
        water= water+(min(left[i],right[i])-arr[i])
    print(water)
        
#
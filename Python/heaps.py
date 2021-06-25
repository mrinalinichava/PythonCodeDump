def heapify(arr,n,i):
    largest =i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[l]>arr[largest]):
        largest=l
    if(r<n and arr[r]>arr[largest]):
        largest=r
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def buildheap(arr,n):
    stindex=n//2-1
    for i in range(stindex,-1,-1):
        heapify(arr,n,i)
def printHeap(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

arr = [ 1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17 ]
n=len(arr)
buildheap(arr,n)
printHeap(arr,n)
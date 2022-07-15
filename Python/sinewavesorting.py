arr =[10, 5, 6, 3, 2, 20, 100]

def wave(arr):
    n = len(arr)
    for i in range(0,n-1,2):
        if(i<n-1 and arr[i]<arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
        if(i>0 and arr[i]<arr[i-1]):
            arr[i],arr[i-1]=arr[i-1],arr[i]
    return arr
def sinewave(arr):
    n= len(arr)
    for i in range(1,n-1,2):
        if(arr[i]<arr[i-1]):
            arr[i],arr[i-1]=arr[i-1],arr[i]
        if(arr[i]<arr[i-1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

def rearrangeAlternatively(arr):
    n= len(arr)
    for i in range(1,n-1,2):
        arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr

b= [1,2,3,4,5,6,7]
print(rearrangeAlternatively(b))


            

# print(sinewave(arr))
# print(wave(arr))
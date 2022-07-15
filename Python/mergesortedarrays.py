arr1 = [1, 5, 9, 10, 15, 20 ]
arr2 =[ 2, 3, 8, 13 ]
  
def merge(n, m):
    i = 0
    temp = 0
  
    # While loop till last element
    # of array 1(sorted)
    # is greater than first element
    # of array 2(sorted)
    while (arr1[n - 1] > arr2[0]):
        if (arr1[i] > arr2[0]):
  
            # Swap arr1[i] with first element
            # of arr2 and sorting the updated
            # arr2(arr1 is already sorted)
            # swap(arr1[i],arr2[0])
            temp = arr1[i]
            arr1[i] = arr2[0]
            arr2[0] = temp
            arr2.sort()
        else:
            i=i+1
      
  
  
# Driver code
if __name__ == '__main__':
    merge(len(arr1), len(arr2))
  
    print("After Merging \nFirst Array: ")
    print((arr1))
  
    print("Second Array:  ")
    print((arr2))
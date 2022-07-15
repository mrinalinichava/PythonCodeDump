arr=[[1,2,3],[4,5,6],[7,8,9]]
def spiralMatrix(arr):
    top=0
    bottom = len(arr)-1
    left =0
    right = len(arr)-1

    while(left<right and top<bottom):
        while(left<=right):
            for i in range(left,right+1):
                print(arr[top][i])
            break
        top=top+1

        while(top<bottom):
            for i in range(top,bottom+1):
                print(arr[i][right])
            break
        right = right-1

        while(right>=left):
            for i in range(right,left-1,-1):
                print(arr[bottom][i])
            break
        bottom=bottom-1
        while(bottom>=top):
            for i in range(bottom,top-1,-1):
                print(arr[i][left])
            break
        left=left+1
        # left=left+1
        # top=top+1
        # bottom=bottom-1
        # right=right-1
    # while(right>left):

    #     print(arr[right][bottom])
    #     right= right-1
    


print(spiralMatrix(arr))
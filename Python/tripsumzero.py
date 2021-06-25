def tripsumzero(arr,n):
    flag=False
    for i in range(n-1):
        s=[]
        for j in range(i+1,n):
            # print(arr[j])
            x = -(arr[i]+arr[j])
            if x in s:
                print(x,arr[i],arr[j])
                flag=True
            else:
                s.append(arr[j])
    if(flag==False):
        print("No triplet found")
arr=[0,-1,2,-3,1]
tripsumzero(arr,len(arr))
            
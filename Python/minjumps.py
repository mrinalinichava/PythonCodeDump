a=[1,3,5,8,9,2,6,7,6,8,9]
def minjumps(a):
    n= len(a)
    minjump=[]
    jumps=[0]*n
    minjump.append(0)
    for i in range(1,n):
        jumps[i] = float('inf')
        for j in range(i):
            if((i<=j+a[j]) and jumps[j]!=float('inf')):
                jumps[i]=min(jumps[j]+1,jumps[i])
                break
    return jumps[n-1]

print(minjumps(a))
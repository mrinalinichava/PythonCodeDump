def fibonacci(n):
    ans = [0]*n
    ans[0]=0
    ans[1]=1
    for i in range(2,n):
        ans[i]=ans[i-1]+ans[i-2]
    return ans
print(fibonacci(4))
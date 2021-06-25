# MAX PRODUCT OF TWO INTEGRES IN ARRAY
#[-10,-3,5,6,-2]
#O(n^2)
def max_prod(a):
    max_prod=0
    cur_prod=0
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            cur_prod=a[i]*a[j]
            if max_prod<cur_prod:
                max_prod=cur_prod
    return max_prod
a=[-10,-3,5,5,-2]
print(max_prod(a))


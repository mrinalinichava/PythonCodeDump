def factorial(num):
    res=[0]*500
    res[0]=1
    resize=1
    for i in range(2,num+1):
        resize=multiply(i,res,resize)
    for i in range(resize-1,-1,-1):
        print(res[i])


def multiply(number,res,n):
    carry =0
    for i in range(n):
        prod = number*res[i]+carry
        res[i]=prod%10
        carry = prod/10
    while(carry):
        # n=n+1
        res[n]=carry%10
        carry=carry/10
        n=n+1
    return n
print(factorial(10))
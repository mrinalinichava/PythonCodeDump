

# def sumcons(a):
#     l=[]
#     i=0
#     while(i<=len(a)-1):
#         count=1
#         k=a[i]
#         j=i
#         while(j<len(a)-1):
#             if(a[j]==a[j+1]):
#                 count=count+1
#                 j=j+1
#             else:
#                 break
#         l.append(k*count)
#         i=j+1
#     return l
# a=[1,4,4,4,0,4,3,3,1]  
# print(sumcons(a))

def sumi(a,k):
    n=len(a)
    for i in range(n):
        for j in range(i,n):
            if(a[i]+a[j]==k):
                print("found")
                

k=5
a=[4,5,7,3,2]
print(sumi(a,k))

#How to find Pythagorean triplets in an array
# from math import sqrt
# def triplets(a):
#     n= len(a)
#     for i in range(n):
#         a[i]=a[i]**2
#     a.sort()
#     for i in range(n-1,1,-1):
#         b=0
#         c=i-1
#         while(b<c):
#             if(a[i]==a[b]+a[c]):
#                 print("triplet found",sqrt(a[b]),sqrt(a[c]),sqrt(a[i]))
#                 b=b+1
#                 c=c-1
#             else:
#                 if(a[b]+a[c]<a[i]):
#                     b=b+1
#                 else:
#                     c=c-1
#     print("THERE ARE NO TRIPLETS")
# a=[3,1,4,5,6]
# print(triplets(a))
                

#Chocolate Distribution Problem
def chocolate(a,k):
    a.sort()
    i=0
    n=len(a)
    mini=999999
    start =0
    end=0
    while(i<n-k+1):
        mini =min(mini,a[i+k-1]-a[i])
        i=i+1
    return mini

a=[7,3,2,4,9,12,5,6]
print(chocolate(a,7))

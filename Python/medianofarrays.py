a=[1,3,5,7,9,11]
b=[2,4,6,8,10,12]
# def medofarr(a1,a2):
#     m= len(a1)
#     n= len(a2)
#     k=[]
#     c=0
#     i=j=0
#     #m1=m2=-1
#     while(c<n+1 and i<m and j<n):
#         if(a1[i]<a2[j]):
#             k.append(a1[i])
#             i=i+1
#         else:
#             k.append(a2[j])
#             j=j+1
#         if(i==m):
#             k.append(a2[0])
#             break
#         if(j==n):
#             k.append(a1[0])
#             break
#     return (k[-1]+k[-2])/2
# print(medofarr(a1,a2))


#Median of sorted arrays of diff sizes 
# def medianofsorted(a,b):
#     i=j=k=l=0
#     c=0
#     m=len(a)
#     n=len(b)
#     med=(m+n)//2
#     if((m+n)%2==1):
#         for c in range(med+1):
#             if(i!=m and j!=n):
#                 if(a[i]<b[j]):
#                     k=a[i]
#                     i=i+1
#                 else:
#                     k=b[j]
#                     j=j+1
#             if



## recursive method

def mediansorted(a,b):
    m=len(a)
    n=len(b)
    m1=med(a)
    m2=med(b)
    if(m1<m2):
        return mediansorted(a[(n//2):],b[:n//2+1])
    else:
        return mediansorted(a[:n//2+1],b[n//2+1:])

def med(a):
    n=len(a)
    if(n%2==0):
        return (a[n//2]+a[n//2-1])/2
    else:
        return a[n//2]
print(mediansorted(a,b))
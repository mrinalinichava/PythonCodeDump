#inplace merge two sorted arrays
#x=1,4,7,8,10
#y=2,3,9

# def sortinplace(a,b):
#     m=len(a)
#     n=len(b)
#     i=0
#     j=0
#     for i in range(m):
#         if(a[i]>b[0]):
#             a[i],b[0]=b[0],a[i]
#             temp=b[0]
#             for j in range(n):
#                 if(b[j]<temp):
#                     b[j-1],b[j]=b[j],b[j-1]
#             # b[j-1]=temp
#     print(a)
#     print(b)
# a=[2,8,9,12]
# b=[1,3,5]
# sortinplace(a,b)    
            
# UNION OF tWO soRTED ARRAYS

# def unionarr(a1,a2):
#     i=j=0
#     m=len(a1)
#     n=len(a2)
#     l=[]
#     while(i<m and j<n):
#         if(a1[i]<a2[j]):
#             l.append(a1[i])
#             i=i+1
#         elif(a1[i]>a2[j]):
#             l.append(a2[j])
#             j=j+1
#         else:
#             l.append(a1[i])
#             i=i+1
#             j=j+1
#     while(i<m):
#         l.append(a1[i])
#     while(j<n):
#         l.append(a2[j])
#     return l
# print(unionarr(a1,a2))

a1=[1,4,5,7,9]
a2=[2,3,4,6,9]
def inters(a1,a2):
    m=len(a1)
    n=len(a2)
    i=j=0
    l=[]
    while(i<m and j<n):
        if(a1[i]>a2[j]):
            j=j+1
        elif(a1[i]<a2[j]):
            i=i+1
        else:
            l.append(a1[i])
            i=i+1
            j=j+1
    return l
print(inters(a1,a2))


        


        
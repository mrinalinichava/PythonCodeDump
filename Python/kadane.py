#MAX SUM CONTIGUOUS SUBARRAY

# a=[-2,-3,4,-1,-2,1,5,-3]
# def maxsumsubarray(a):
#     n=len(a)
#     maxsf=curmax=0
#     for i in range(n):
#         curmax=curmax+a[i]
#         if(curmax<0):
#             curmax=0
#         if(maxsf<curmax):
#             maxsf=curmax
#     return maxsf


#handlinng negative elements
# a=[-1,-2,-3,0,-1,-8,-9]
# def maxsum(a):
#     curmax=maxsf=a[0]
#     for i in range(1,len(a)):
#         curmax=max(curmax,curmax+a[i])
#         maxsf=max(maxsf,curmax)
#     return maxsf
# print(maxsum(a))


# print the array
a=[-2,-3,4,-1,-2,1,5,-3]
def maxsum(a):
    maxy=curmax=0
    n= len(a)
    st=e=0
    s=0

    for i in range(len(a)):
        curmax=curmax+a[i]
        if(curmax<0):
            curmax=0
            s=i+1
        if(maxy<curmax):
            maxy=curmax
            st=s
            e=i
    print(a[st:e+1])
print(maxsum(a))
            


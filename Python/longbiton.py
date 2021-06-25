#FIND THE LONGEST BIOTONIC SEQUENCE
#FIRST ELEMENTS IN INCREASING ORDER THEN IN DECREASING

#[3,5,8,4,5,9,10,8,5,3,4]
# def long_bio(a):
#     flag=0
#     n=len(a)
#     count=0
#     start=0
#     maxcount=0
#     for i in range(n):
#         start=i
#         for j in range(n):
#             if(a[j+1]>a[j] and flag==1):
#                 break
#             if(a[j+1]>a[j]):
#                 count=count+1
#             if(a[j+1]<a[j]):
#                 count=count+1
#                 flag=1
#         s=a[start:start+count]
#     return s   
# a=[3,5,8,4,9,10,8,5,3,4]
# print(long_bio(a))



# def bioseq(a):
#     i=0
#     c=0
#     d=0
#     maxc=0
#     flag=0
#     start=0
#     end=0
#     n=len(a)
#     while(i<n):
#         c=0
#         d=0
#         #maxc=0
#         for j in range(i,n-1):
#             if((a[j+1]>a[j])):
#                 start=i
#                 c=c+1
#             if(a[j+1]<a[j] and flag==0):
#                 d=d+1
#             elif(a[j+1]>a[j] and flag==1):
#                 end=j
#                 break
#         if(maxc<c+d):
#             maxc=c+d
#         i=i+1
#     print(start)
#     print(end)
#     return maxc
# a=[3,5,8,4,9,10,8,5,3,4]
# print(bioseq(a))

######################################################################

# def biton(a):
#     n=len(a)
#     if(n==0):
#         return 0
#     maxlen=1
#     start=0
#     nextstart=0
#     i=0
#     while(i<n-1):
#         while(i<n-1 and a[i+1]>a[i]):
#             i=i+1
#         while(i<n-1 and a[i]>a[i+1]):
#             if(i<n-1 and a[i]>a[i+1]):
#                 nextstart=i+1
#             i=i+1
#         maxlen=max(maxlen,i-(start-1))
#         start=nextstart
#     return maxlen
# a=[12,4,78,90,45,23]
# print(biton(a))

def biton(a):
    n=len(a)
    if(n==1):
        return a
    inlen=1
    declen=0
    flag=0
    maxlen=0
    endi=0
    for i in range(n):
        if(a[i]>a[i-1]):
            declen=0
            if(flag):
                inlen=1
                flag=0
            inlen=inlen+1
        elif(a[i]<a[i-1]):
            flag=1
            declen=declen+1
        else:
            if(flag):
                declen=declen+1
            else:
                inlen=inlen+1
        if(maxlen<inlen+declen):
            maxlen=inlen+declen
            endi=i
            start =endi-maxlen+1
    return a[start:endi+1]
a=[12,4,78,90,45,23]
print(biton(a))
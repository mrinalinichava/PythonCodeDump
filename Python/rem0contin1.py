# INDEX OF 0 TO BE REMOVED TO FORM CONTINUOUS 1'S

#a=[0,0,1,0,1,1,1,0,1,1]
# def removezero(a):
#     n=len(a)
#     left=0
#     right=0
#     indexzero=0
#     finzero=0
#     maxc=0
#     for i in range(n):
#         if(a[i]==1):
#             right=right+1
#         else:
#             left=right
#             right=0
#             indexzero=i
#         if(maxc<left+right):
#             maxc=left+right
#             finzero=indexzero
#     return finzero


# a=[0,0,1,0,1,1,1,0,1,1]
# print(removezero(a))

def remz(a):
    n=len(a)
    maxlen=-1
    curlen=-1
    prev=-1
    req=-1
    prevprev=-1
    for i in range(n):
        if(a[i]==0):
            if(prevprev!=-1):
                curlen=i-prevprev-1
                if(curlen>maxlen):
                    maxlen=curlen
                    req=prev
            prevprev=prev
            prev=i
    if(maxlen==-1):
        if(prevprev==-1):
            if(prev>n-prevprev-1):
                req=prevprev
            else:
                req=prev
        else:
            req=prev
    return req

a=[0,0,1,0,1,1,1,0,1,1]
print(remz(a))


    # for i in range(n):
    #     if(a[i]==0 and i>0):
    #         if(a[i-1]==1 and a[i+1]==1):
    #             p=i-1
    #             q=i+1
    #             c1=0
    #             c2=0
    #             while(p>0):
    #                 if(a[p]==1):
    #                     c1=c1+1
    #                 elif(a[p]==0):
    #                     break
    #                 p=p-1
    #             while(q<n-1):
    #                 if(a[q]==1):
    #                     c2=c2+1
    #                 elif(a[q]==0):
    #                     break
    #             maxc=max(maxc,c1+c2)
    # return maxc


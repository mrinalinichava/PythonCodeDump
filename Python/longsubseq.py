a=[100,4,200,1,3,2]
# def longconsub(a):
#     s=set()
#     res=0
#     for ele in a:
#         s.add(ele)
#     for i in range(len(a)):
#         if((a[i]-1) not in s):
#             j=a[i]
#             while(j in s):
#                 j=j+1
#             res=max(res,j-a[i])
#     return res
# print(longconsub(a))
        
def longsubs(a):
    a.sort()
    c=0
    s=[]
    res=0
    print(a)
    for i in range(1,len(a)):
        if(a[i]!=a[i-1]):
            s.append(a[i])
    for i in range(len(s)):
        if(i>0 and s[i]==s[i-1]+1):
            c=c+1
        else:
            c=1
        res=max(res,c)
    return res     
print(longsubs(a))
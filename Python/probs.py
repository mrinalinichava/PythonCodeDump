# def compstring(s1,s2):
#     n1=len(s1)
#     n2=len(s2)
#     start= n1-n2
#     if(s1[start]!=s2[0] or s1[-1]!=s2[-1]):
#         return False
#     else:
#         if(s1[start:]==s2[:]):
#             return True

# s1="abcdef"
# s2="defg"
# print(compstring(s1,s2))

############################################################################################

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

############################################################################################


def nextbig(num):
    s=list(num)
    n=len(s)
    l=[]
    last =s[-1]
    i=n-1
    while(i>0):
        if(s[i-1]>s[i]):
            i=i-1
            continue
        else:
            d1=i-1
            break
    for i in range(d1+1,n):
        if(s[i]>s[d1]):
            l.append(int(s[i]))
    print(s)
    print(l)
    ind1 =s.index(str(min(l)))

    s[d1],s[ind1]=s[ind1],s[d1]
    sorted(s[d1+1:])
    return "".join(s)
s="25945678"
print(nextbig(s))   
    

############################################################################################

# def missingnum(a):
#     l=list(a)
#     s=set(l)
#     sum2=0
#     n=len(s)+1
#     sumi =(n*(n+1))/2
#     print(sumi)
#     for ele in s:
#         sum2=sum2+ int(ele)
#     print(sumi-sum2)
# aq="12444556789"
# missingnum(aq)
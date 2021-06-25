#subarry with 0 sum exists or not
# def sub(a):
#     s=set()
#     sum=0
#     for ele in a:
#         sum=sum+ele
#         if(sum==0 or sum in s):
#             return True
#         s.add(sum)
#     return False
# a=[-3,3,2,1,6]
# print(sub(a))


###############################################################

#print all the subarrays with sum 0

# arr = [3,4,-7,3,1,3,1,-4,-2,-2]
# ii = 0

# while(ii < len(arr)):
#     tmp = []
#     sum = 0
#     for i in arr[ii:]:
#         #print(i)
#         if i == 0:
#             print(i)

#         sum = sum+i
#         tmp.append(i)
#         if sum == 0:
#             print(tmp)
#     ii+=1

def subzero(a):
    n=len(a)
    sumy=0
    d={}
    c=0
    for i in range(n):
        sumy=sumy+a[i]
        if(sumy==0):
            print(a[:i+1])
            c=c+1
        if(sumy in d and sumy!=0):
            print(a[d[sumy]+1:i+1])
            c=c+1
        else:
            d[sumy]=i
    return c

a=[3,4,-7,3,1,3,1,-4,-2,-2]
print(subzero(a))

###############################################################

#LONGEST SUBARRAY WITH GIVEN SUm
# def subgivsum(a,num):
#     l=0
#     n=len(a)
#     end_indx=0
#     for i in range(n):
#         sumy=0
#         for j in range(i,n):
#             sumy=sumy+a[j]
#         if(sumy==num):
#             if(l<i-j+1):
#                 l=0
#                 end_indx=j
#     print((end_indx-l+1,end_indx))

#USING HASHMAP

# def sub_sum(a,k):
#     d={}
#     n=len(a)
#     sumy=0
#     maxlen=0
#     for i in range(n):
#         sumy=sumy+a[i]
#         if(sumy==k):
#             maxlen=i+1
#         elif(sumy-k in d):
#             maxlen=max(maxlen,i-d[sumy-k])
#         if(sumy not in d):
#             d[sumy]=i
#     return maxlen
# a=[10, 5, 2, 7, 1, 9]
# print(sub_sum(a,15))


###############################################################


#[1,0,0,0,0,1,1,1,0,0]
#SUB ARRAY WITH EQUAL NUMBER OF 0's and 1's
# def subeq(a):
#     n=len(a)
   
#     l=0
#     #maxlen=0
#     for i in range(n):
#         c1=0
#         c2=0
#         for j in range(i,n):
#             if(a[j]==0):
#                 c1=c1+1
#             if(a[j]==1):
#                 c2=c2+1
#             if(c1==c2):
#                 if(l<j-i+1):
#                     l=j-i+1
#     return l
# a=[1,0,0,0,0,1,1,1,0,0]
# print(subeq(a))       

#USING HASHMAP

# def subeq(a):
#     sumy=0
#     d={}
#     maxlen=0
#     n=len(a)
#     for i in range(n):
#         if(a[i]==0):
#             a[i]=-1
#     for i in range(n):
#         sumy=sumy+a[i]
#         if(sumy==0):
#             maxlen=max(maxlen,i+1)
#         if(sumy in d):
#             maxlen=max(maxlen,-d[sumy])
#         elif(sumy not in d):
#             d[sumy]=i
#     return maxlen
# a=[1,0,1,0]
# print(subeq(a))    


# sums up to the given array

# from collections import OrderedDict
# from collections import defaultdict
# arr = [8, 7, 2, 5, 3, 1]
# def sumarr(a,k):
#     d={}
#     for i,e in enumerate(a):
#         if(k-e in d):
#             print("ele found at",d[k-e],i)
#             return
#         d[e]=i
#     print("No pair found")
    # a.sort()
    # i=0
    # j=len(a)-1
    # while(i<=j):
    #     if(a[i]+a[j]==k):
    #         print("Pairforunf at",i,j)
    #         break
    #     elif(a[i]+a[j]<k):
    #         i=i+1
    #     else:
    #         j=j-1
    # print("False")
# print(sumarr(arr,10)

        
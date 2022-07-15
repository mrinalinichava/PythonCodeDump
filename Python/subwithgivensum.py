# def subgivensum(a,k):
#     n=len(a)
#     curs=0
#     d={}
#     for i in range(n):
#         curs=curs+a[i]
#         if(curs==k):
#             print("found btw",0,"to",i)
#         if(curs-k in d):
#             print("sum found between")
#             print(d[curs-k]+1,"to",i)
#             return
#         d[curs]=i
#     print("No foudn")
    
# a=[10,2,-2,-20,10]
# print(subgivensum(a,-1))

#Count the subarrays with given sum
from collections import defaultdict
def countSub(arr,k):
    n = len(arr)
    d= defaultdict(int)
    count=sumy =0
    for ele in arr:
        sumy = sumy+ele
        if(sumy==k):
            count=count+1
        if(sumy-k in d):
            count=count+1
        d[sumy]=d[sumy]+1
    return count
arr= [10,2,-2,-20,10]
print(countSub(arr,-10))

# from collections import defaultdict
# def countSubarrayswithSumK(a, K):
#     n = len(a)
#     hash = defaultdict(lambda: 0)
#     count = 0
#     sum = 0
#     for i in range(n):
#         sum += a[i]
#         if sum == K:
#             count += 1
#         if (sum - K) in hash:
#             count += hash[sum - K]
#         hash[sum] += 1
#     return count
# arr= [10,2,-2,-20,10]
# print(countSubarrayswithSumK(arr,-10))



arr = [10, 2, -2, -20, 10]
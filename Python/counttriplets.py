# from collections import defaultdict
# def countTriplets(arr):
#     maxi = max(arr)
#     print(maxi)
#     count = 0
#     d=defaultdict(int)
#     for ele in arr:
#         d[ele]=d[ele]+1
#     #case-1 (000)(nc3)
#     count = count + (d[0]*(d[0]-1)*(d[0]-2))//6
#     #case 2 (0,x,x)
#     for i in range(1,maxi+1):
#         count = count+ (d[0]*d[i]*(d[i]-1))//2
#     #case-3(x,x,2x)
#     for i in range(1,(maxi+1)//2):
#         count = count + (d[i]*(d[i]-2)//2)*d[2*i]
#     for i in range(1,maxi+1):
#         for j in range(i+1,maxi-i+1):
#             count = count + d[i]*d[j]*d[i+j]
#     return count

# A = [1, 2, 3, 4, 5]
# N = 5
# print(countTriplets(A))

def count_Triplets(A, n):
    max_val = 0
    for i in range(n):
        max_val = max(max_val, A[i])
 
    freq = [0 for i in range(max_val + 1)]
 
    for i in range(n):
        freq[A[i]] += 1
 
    count = 0 
 
 
    count += (freq[0] * (freq[0] - 1) *
           (freq[0] - 2) // 6)
 
    for i in range(1, max_val + 1):
        count += (freq[0] * freq[i] *
               (freq[i] - 1) // 2)
 
    for i in range(1, (max_val + 1) // 2):
        count += (freq[i] *
               (freq[i] - 1) // 2 * freq[2 * i])
 
    for i in range(1, max_val + 1):
        for j in range(i + 1, max_val - i + 1):
            count += freq[i] * freq[j] * freq[i + j]
 
    return count
 
 
A = [1, 2, 3, 4, 5]
N = 5
print(count_Triplets(A, N))
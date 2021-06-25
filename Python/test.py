# a=[[0 for x in range(3)]for y in range(3)]
# for i in range(3):
#     for  j in range(3):
#         a[i][j]=int(input())
# for i in range(3):
#     print("\n")
#     for j in range(3):
#         print(a[i][j],end=" ")
# print("\n")



# d={}
# for i in range(10):
#     if(d[i]==0):
#         d[i]=d[i]+1
# print(d)

# from collections import defaultdict
# d=defaultdict(lambda:0)
# c=0
# d[1]=2
# for i in range(10):
#     if(d[i]==0):
#         c=c+1
#     d[i]=d[i]+1
# print(d)

# t=12^12
# print(t)
# if(t==0):
#     print("Yes")

a='geeksforgeeks'
b='olx'
mini=300
for i in b:
    if i in a:
        ind=a.index(i)
        mini=min(mini,ind)
    else:
        print("$")
print(mini)

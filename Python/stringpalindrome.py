#   FIND IF A STRING IS PALINDROME OR NOT
# s='abcba'
# def palindrome(s):
#     i=0
#     n=len(s)
#     j=n-1
#     while(i<=j):
#         if(s[i]==s[j]):
#             i=i+1
#             j=j-1
#             continue
#         elif(s[i]!=s[j]):
#             return False
            
#     return True
# print(palindrome(s))
    
#REVERSE WITHOUT AFFECTING THE SPECIAL CHARACTERS

# s="a,b&c,d*"
# s="a!!!b.c.d,e'f,ghi"
# def reverse(s):
#     n=len(s)
#     i=0
#     j=n-1
#     s=list(s)
#     print(s)
#     while(i<=j):
#         temp =s[i]
#         if(not s[i].isalpha()):
#             i=i+1
#         elif(not s[j].isalpha()):
#             j=j-1
#         else:
#             s[i],s[j]=s[j],s[i]
#             i=i+1
#             j=j-1
#     return " ".join(s)
# print(reverse(s))    

#FIND DUPLICATE CHARACTERS OF A STRING   
# from collections import defaultdict 
# s="hello"
# def duplicate(s):
#     d=defaultdict(int)
#     for ele in s:
#         d[ele]=d[ele]+1
#     for key in d.keys():
#         if(d[key]>1):
#             print(key)
# print(duplicate(s))


#TWO STRINGS ARE ROTATIONS OF EACH OTHER
# s1="ABACD"
# s2="CDABA"
# def rotations(s1,s2):
#     s=s1+s1
#     if(len(s1)!=len(s2)):
#         return False
#     if(s2 in s):
#         return True
#     else:
#         return False
# print(rotations(s1,s2))



#STRING IS A VALID SHUFFLE OF TWO DISTINCT STRINGS

# def validshuffle(a,b,c):
#     m=len(a)
#     n=len(b)
#     dp =[[False]*(n+1) for i in range(m+1)]
#     if((m+n)!=len(c)):
#         return False
#     for i in range(m+1):
#         for j in range(n+1):
#             if(i==0 and j==0):
#                 dp[i][j]=True
#             elif(i==0):
#                 if(b[j-1]==c[j-1]):
#                     dp[i][j]=dp[i][j-1]
#             elif(j==0):
#                 if(a[j-1]==c[j-1]):
#                     dp[i][j]=p[i-1][j]
#             elif(c[i+j-1]==a[i-1] and c[i+j-1]!=b[j-1]):
#                 dp[i][j]=dp[i-1][j]
#             elif(c[i+j-1]==b[i-1] and c[i+j-1]!=a[j-1]):
#                 dp[i][j]=dp[i][j-1]
#             else:
#                 dp[i][j]=(dp[i][j-1] or dp[i-1][j])
#     return dp[m][n]

# a="aab"
# b="axy"
# c="abaayx"
# print(validshuffle(a,b,c))


#NAIVE PATTERN SEARCH

# def naivepattern(s,text):
#     m=len(s)
#     n=len(text)

#     for i in range(n-m+1):
#         j=0
#         while(j<m):
#             if(text[i+j]!=s[j]):
#                 break
#             j=j+1
#         if(j==m):
#             print("pattrn found",i)
# text="AABAACAADAABAAABAA"
# s="AABA"
# print(naivepattern(s,text))

#STRING ANAGRAM
# s1="abcd"
# s2="bdca"

# def anagrams(s1,s2):

#     for ele in s2:
#         s1=s1.replace(ele,"")
#     if(s1==""):
#         return True
#     return False
        
# print(anagrams(s1,s2))   

#PRINT SECOND MOST FREQ ELEMENT
# from collections import Counter  
    
# def secondFrequent(a):    
#     dict = Counter(a)  
#     print(type(dict))
#     value = sorted(dict.values(), reverse=True)  

#     secondLarge = value[1]    
#     for (key, val) in dict.items():  
#         if val == secondLarge:  
#             print (key)  
#             return
# a=['aaa','bbb','ccc','bbb','aaa','aaa']
# print(secondFrequent(a))

#SORT ELEMENT LIST BY FREQUENCY

# def sortbyfreq(a):
    
# PATTERN SEARCH

# def patfind(p,s):
#     m=len(s)
#     n=len(p)
#     for i in range(m-n+1):
#         j=0
#         while(j<n):
#             if(p[j]!=s[i+j]):
#                 break
#             j=j+1
#         if(j==n):
#             print("found at index",i)
#     print("not found")
# p="abcd"
# s="abcddhbhabcdjk"
# print(patfind(p,s))

t= int(input())
l=[]
for i in range(t):
    l.append(input())
print(l)
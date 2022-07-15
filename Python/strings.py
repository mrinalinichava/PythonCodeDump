#all the palindromes
def palindromes(s):
    count=0
    for i in range(0,len(s)):
        count =count+findall(s,i-1,i+1)
        count=count +findall(s,i,i+1)
    return count
    
def findall(s,i,j):
    count=0
    while(i>=0 and j<len(s)):
        if(s[i]!=s[j]):
            break
        print(s[i:j+1])
        count=count+1
        i=i-1
        j=j+1
    return count
    

print(palindromes("aabbbaa"))

#longest subsequence without repeating characters
string ="geeksforgeeks"
def longestsubstr(string):
    n= len(string)
    lastindex={}
    maxlen=0
    start=0
    end=0
    for i in range(n):
        if(string[i] in lastindex):
            start= max(start,lastindex[string[i]]+1)
        maxlen= max(maxlen,i-start+1)
        lastindex[string[i]]=i
    return maxlen
print(longestsubstr(string))
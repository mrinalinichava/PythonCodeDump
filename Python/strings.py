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
#Length of the longest substring without repeating characters
#   ABZXHYAUWILG

def longest_sub(s):
    n=len(s)
    visited=[-1]*256
    curlen=1
    maxlen=1
    prev_indx=0
    visited[ord(s[0])]=0
    for i in range(1,n):
        prev_indx=visited[ord(s[i])]
        if(prev_indx==-1 or i-curlen>prev_indx):
            curlen=curlen+1
        else:
            if(curlen>maxlen):
                maxlen=curlen
            curlen=i-prev_indx
        visited[ord(s[i])]=i
    if curlen>maxlen:
        maxlen=curlen
    return maxlen
s="ABCDABcdefghijab"
print(longest_sub(s))     

        


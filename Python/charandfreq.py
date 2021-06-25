s='geeksforgeeks'
def charfreq(s):
    freq=[0]*26
    k=''
    for ele in s:
        freq[ord(ele)-ord('a')]=freq[ord(ele)-ord('a')]+1
    for ele in s:
        if(freq[ord(ele)-ord('a')]!=0):
            k=k+ele+str(freq[ord(ele)-ord('a')])
            # k.join(ele)
            # k.join(freq[ord(ele)-ord('a')])
            #print(ele,freq[ord(ele)-ord('a')])
            freq[ord(ele)-ord('a')]=0
    return k
print(charfreq(s))
print("\U0001F600")
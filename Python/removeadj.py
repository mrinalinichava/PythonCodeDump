def dup(s):
    char=list(s)
    k=0
    n=len(s)
    i=1
    while(i<n):
        if(char[i-1]!=char[i]):
            char[k]=char[i-1]
            k=k+1
        else:
            while(i<len(char) and char[i-1]==char[i]):
                i=i+1
        i=i+1
    char[k]=char[i-1]
    k=k+1
    s="".join(char[:k])
    if(k!=n):
        return dup(s)
    return s
print(dup("AABCDE"))
        
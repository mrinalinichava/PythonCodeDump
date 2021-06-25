def subgivensum(a,k):
    n=len(a)
    curs=0
    d={}
    for i in range(n):
        curs=curs+a[i]
        if(curs==k):
            print("found btw",0,"to",i)
        if(curs-k in d):
            print("sum found between")
            print(d[curs-k]+1,"to",i)
            return
        d[curs]=i
    print("No foudn")
    
a=[10,2,-2,-20,10]
print(subgivensum(a,-1))
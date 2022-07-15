#User function Template for python3
from collections import defaultdict
class Solution:

    def getSubstringWithEqual012(self, Str):
        # code here
        #012000 # count is 2
        d= dict()
        d[(0,0)]=1
        zero,one,two,count,flag,key  =0,0,0,0,0,0
        for ele in Str:
            if(ele == '0'):
                zero+=1
            elif(ele== '1'):
                one += 1
            else:
                two +=1
            temp = (zero-one,one-two)
            #print(temp)
            if(temp not in d):
                d[temp]=1
            else:
                count = count+d[temp]
                d[temp]=d[temp]+1
        return count
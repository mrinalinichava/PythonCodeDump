import math
import time
def ps(a,b):
    for ele in a:
        for bl in b:
            x=math.sqrt(ele*bl)
            #print(x)
            if(x.is_integer()):
               print((ele,bl))
              
a=[1,2,3,4]
b=[4,5,6,7]

start_time = time.time()

ps(a,b)
print((time.time()-start_time))
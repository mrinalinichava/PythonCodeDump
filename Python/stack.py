class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.size=0
    def push(self,data):
        self.size+=1
        self.q2.put(data)
        while(self.q1):
            temp = self.q1.get()
            self.q2.put(temp)
        self.q1,self.q2= self.q2,self.q1
    def pop(self):
        if(self.q1.empty()):
            return -1
        self.q1.get()
        size=size-1

class Stack1:
    def __init__(self):
        self.arr=[]
        self.top=-1
        self.max= 100
        
    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def isFull(self):
        if(self.top==self.max-1):
            return True
        else:
            return False
    def push(self,data):
        if(self.isFull()):
            print("stack is full")
            return 
        else:
            self.arr.append(data)
                
    def pop(self):
        if(self.isEmpty()):
            print("stack is empty")
        else:
            self.top-=1
            return self.arr.pop()
class MinStack(Stack1):
    
    def __init__(self):
        super().__init__()
        self.min = Stack1()
        
    def push(self,data):
        if(self.isEmpty()):
            super().push(data)
            self.min.push(data)
        else:
            super().push(data)
            y = self.min.pop()
            self.min.push(y)
            if(data<=y):
                self.min.push(data)
            else:
                self.min.push(y)
    def pop(self):
        x=super().pop()
        self.min.pop()
        return x
    def getmin(self):
        #super().pop()
        return self.min.pop()
        # x=  self.min.pop()
        # self.min.push(x)
        # return x

s= MinStack()
s.push(10)
s.push(20)
s.push(30)
print(s.arr)
x=s.getmin()
print(x)



class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enq(self,data):
        self.s1.append(data)
    def deq(self):
        if(len(self.s1)==0 and len(self.s2)==0):
            print("queue is empty")
        elif(len(self.s2)==0 and len(self.s1)>0):
            while(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()
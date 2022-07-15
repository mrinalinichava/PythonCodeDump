class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def leftView(root):
        if(root==None):
            return
        q=[]
        ans=[]
        q.append(root)
        while(len(q)):
            size = len(q)
            for i in range(size):
                temp=q.pop(0)
                if(i==size-1):
                    ans.append(temp.data)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)


            # for i in range(1,size+1):
            #     temp = q[0]
            #     q.pop(0)
            #     if(i==1):
            #         ans.append(temp.data)
            #     if(temp.left):
            #         q.append(temp.left)
            #     if(temp.right):
            #         q.append(temp.right)
        return ans

    def topView(root):
        if(root==None):
            return None
        q=[]
        ans=[]
        q.append(root)
        while(len(q)):
            i=0
            size = len(q)
            while(size):
                temp = q.pop(0)
                if(( size==1)):
                    ans.append(temp.data)
                elif(i==0 or i==size-1):
                    ans.append(temp.data)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                size=size-1
                i=i+1
        return ans

root = newNode(10)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(8)
root.right.right = newNode(15)
root.right.left = newNode(12)
root.right.right.left = newNode(14)
root.right.right.right = newNode(15)
print(newNode.leftView(root))
# if __name__ == '__main__':
 
#     root = newNode(10)
#     root.left = newNode(2)
#     root.right = newNode(3)
#     root.left.left = newNode(7)
#     root.left.right = newNode(8)
#     root.right.right = newNode(15)
#     root.right.left = newNode(12)
#     root.right.right.left = newNode(14)
#     print(newNode.leftView(root))
                    
                
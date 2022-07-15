class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def levelOrder(root,k):
        if(root==None):
            return
        q=[]
        res=0
        q.append(root)
        level= 0
        while(len(q)>0):
            size = len(q)
            result = []
            while(size>0):
                temp = q.pop(0)
                result.append(temp.data)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                size=size-1
            if(level==k-1):
                return (len(result))
            level =level+1
        return 0

    def avgOfLevels(root):
        if(root==None):
            return
        q=[]
        ans=[]
        q.append(root)
        while(len(q)):
            size = len(q)
            res=[]
            while(size>0):
                temp = q.pop(0)
                res.append(temp.data)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                size=size-1
            ans.append(sum(res)/len(res))
        return ans

            
        return ans
if __name__ == '__main__':
 
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    # print(newNode.levelOrder(root,3))
    print(newNode.avgOfLevels(root))

                    
                
#python3 Program to print zigzag traversal of binary tree 
import collections 
# Binary tree node 
class Node: 
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

# function to print vertical order traversal of binary tree 
import collections 
def verticalOrder(root): 
    #Your code here
    if(root==None):
        return
    q=[]
    d={}
    hd={}
    q.append(root)
    hd[root]=0
    d[0]=[root.data]
    while(len(q)>0):

        t=q.pop(0)
            
        if(t.left):
            q.append(t.left)
            hd[t.left]=hd[t]-1
            k=hd[t.left]
            if(d.get(k) is None):
                d[k]=[]
            d[k].append(t.left.data)
            
        if(t.right):
            q.append(t.right)
            hd[t.right]=hd[t]+1
            k=hd[t.right]
            if(d.get(k) is None):
                d[k]=[]
            d[k].append(t.right.data)
    d=collections.OrderedDict(sorted(d.items()))
    for ele in d.values():
        for each in ele:
            print(each,end=" ")
# Driver program to check above function 
""" 
Constructed binary tree is 
			1 
		/ \ 
		2	 3 
	/ \ / \ 
	4	 5 6	 7 
			\ / \ 
			8 10 9 
				\ 
				11 
					\ 
					12 
				
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right =Node(8) 
root.right.right.left = Node(10) 
root.right.right.right = Node(9) 
root.right.right.left.right = Node(11) 
root.right.right.left.right.right = Node(12) 
print("Vertical order traversal is ") 
verticalOrder(root)

# This code is contributed by Shweta Singh 

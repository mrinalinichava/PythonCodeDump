# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.left=None
#         self.right=None
#         self.parent=None
# class bst:
#     def __init__(self):

#     	self.root = None
#     def insert(self,root,node):
#         if(root==None):
#             root=node
#         else:
#             if(root.value<node.value):
#                 if(root.right==None):
#                     root.right=node
#                     root.right.parent
#                 else:
#                     self.insert(root.right,node)
#             elif(root.value>node.value):
#                 if(root.left==None):
#                     root.left=node
#                 else:
#                     self.insert(root.left,node)
#     def find(self,root,node):
#         if(root.value==node.value):
#             return True
#         elif(root.value>node.value):
#             return self.find(root.left,node)
#         elif(root.value<node.value):
#             return self.find(root.right,node)
#         else:
#             return False      
#     def inorder(self,root):
#         if(root):
#             self.inorder(root.left)
#             print(root.value) 
#             self.inorder(root.right)
#     def min_val(self,node):
#         curr=node
#         while(curr.left!=None):
#             curr=curr.left
#         return curr

 

#     def delete(self,data):
#         return self.delete_helper(self.root,data)
#     def delete_helper(self,node,val):
#         if(node==None):
#             return node
#         elif(val<node.value):
#             node.left=self.delete_helper(node.left,val)
#         elif(val>node.value):
#             node.right=self.delete_helper(node.right,val)
#         else:
#             if(node.left==None and node.right==None):
#                 node=None
#             elif(node.left==None):
#                 temp=node
#                 node=node.right
#             elif(node.right==None):
#                 temp=node
#                 node=node.left
#             else:
#                 temp =self.min_val(node.right)
#                 node.right=temp.data
#                 node.right=self.delete_helper(node.right,temp.value)
#         return node


# r = Node(50) 
# my_bst=bst()
# my_bst.insert(r,Node(30)) 
# my_bst.insert(r,Node(20)) 
# my_bst.insert(r,Node(40)) 
# my_bst.insert(r,Node(70)) 
# my_bst.insert(r,Node(60)) 
# my_bst.insert(r,Node(80))  
# my_bst.inorder(r)
# print(my_bst.delete(20))
# print("\n")
# my_bst.inorder(r)
# print(my_bst.find(r,Node(20)))     



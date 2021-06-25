# lowest common ancestor
def lowestCommonAncestor(self, root, p, q):
    
    if(root == None):
        return None
    if(root == p or root == q):
        return root
    leftsub = self.lowestCommonAncestor(root.left, p, q)
    rightsub = self.lowestCommonAncestor(root.right, p, q)

    if(leftsub != None and rightsub != None):
        return root
    elif(leftsub != None):
        return leftsub
    else:
        return rightsub

def preorder(root):
    if root:
        return [root.val] + preorder(root.left) + preorder(root.right)  
    else: 
        return []

def inorder(root):
    if root:
        return  inorder(root.left) + [root.val] + inorder(root.right)  
    else: 
        return []

def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
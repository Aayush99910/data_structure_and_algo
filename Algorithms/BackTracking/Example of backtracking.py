# Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes.

def pathExist(root):
  # checking for leaf node 
  if (not root or root.val == 0):
    return False

  # checking for leaf node
  if (root.left == None and root.right == None):
    return True
  
  if (pathExist(root.left)):
    return True
  
  if (pathExist(root.right)):
    return True 
  
  return False 
  
# Determine if a path exists from the root of the tree to a leaf node but also return the path values 

def pathExistWithPath(root, stack):
  # checking for leaf node 
  if (not root or root.val == 0):
    return False 
  
  # if it the root is None and it is not root.value then we can add the value to the stack 
  stack.append(root.val)

  # checking if the node is a leaf node
  if (root.left == None and root.right == None):
    return True 

  if (pathExistWithPath(root, stack)):
    return True 

  if (pathExistWithPath(root, stack)):
    return True 

  # if we have checked both the left and right subtree and we don't get true then that means there is no valid path down in those subtree so we pop the current node 
  stack.pop()
  return False 


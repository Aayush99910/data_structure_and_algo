class TreeNode: 
    def __init__(self, val: int) -> None:
        self.val = val 
        self.left = None
        self.right = None 
    
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def __insert(self, root, val: int):
        if (not root):
            return TreeNode(val)
        
        if (val < root.val):
            root.left = self.__insert(root.left, val)
        elif (val > root.val):
            root.right = self.__insert(root.right, val)

        return root
    
    def findMinimum(self) -> TreeNode:
        curr = self.root
        while (curr.left and curr): #type: ignore
            curr = curr.left 
        
        return curr #type: ignore

    def add(self, val: int) -> None:
        self.root = self.__insert(self.root, val)


def main():
    t1 = Tree()
    t1.add(4)
    t1.add(5)
    t1.add(3)
    t1.add(1)
    t1.add(0)

    print(t1.findMinimum().val)



main()
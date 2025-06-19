class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None

    def left_rotate(self, root):
        # Current root's right child becomes the new root
        new_root = root.right
        # Store the left subtree of the new root
        left_subtree = new_root.left
        # Old root becomes the left child of the new root
        new_root.left = root
        # Stored left subtree becomes the right subtree of the old root
        root.right = left_subtree

        # Uupdate height of the old root first since its subtree changed
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Then update the height of the new root
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def get_height(self, node):
        return -1 if node is None else node.height
    
    def right_rotate(self, root):
        # Current root's left child becomes the new root
        new_root = root.left
        # Store the right subtree of the new root
        right_subtree = new_root.right
        # Old root becomes the right child of the new root
        new_root.right = root
        # Stored right subtree becomes the left subtree of the old root
        root.left = right_subtree

        # Update height of the old root first since its subtree changed
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        # Then update the height of the new root
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def insertion(self, value):
        # If the tree is empty, create a new node as the root
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, call the insertion helper
            self.root = self.insertion_helper(self.root, value)

    def insertion_helper(self, node, value):
        # Base case: If the current node is None, we've found the 
        # insertion point.
        if node is None:
            return Node(value)

        # Recursive case: Descend the tree according to the binary search
        # tree property.
        if value < node.value:
            # Insert in the left subtree.
            node.left = self.insertion_helper(node.left, value)
        else:
            # Insert in the right subtree.
            node.right = self.insertion_helper(node.right, value)

        # After insertion, update the height of the current node.
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Calculate the balance factor to check if the current node is 
        # unbalanced.
        balance = self.get_balance(node)

        # Left Left Case: The inserted node is in the left subtree of the
        # left child.
        if balance > 1 and value < node.left.value:
            # Perform a right rotation to balance the tree.
            return self.right_rotate(node)

        # Left Right Case: The inserted node is in the right subtree of 
        # the left child.
        if balance > 1 and value > node.left.value:
            # First, perform a left rotation on the left child.
            node.left = self.left_rotate(node.left)
            # Then, perform a right rotation on the current node.
            return self.right_rotate(node)

        # Right Right Case: The inserted node is in the right subtree of
        # the right child.
        if balance < -1 and value > node.right.value:
            # Perform a left rotation to balance the tree.
            return self.left_rotate(node)

        # Right Left Case: The inserted node is in the left subtree of the
        # right child.
        if balance < -1 and value < node.right.value:
            # First, perform a right rotation on the right child.
            node.right = self.right_rotate(node.right)
            # Then, perform a left rotation on the current node.
            return self.left_rotate(node)

        # If the node is already balanced, just return it without any 
        # rotations.
        return node

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

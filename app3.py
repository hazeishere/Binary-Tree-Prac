class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


# Create a BST with the given user IDs
user_ids = [50, 30, 70, 20, 40, 60, 80]
bst = BST()

# Insert values into the BST
print("Inserting values into BST:")
for user_id in user_ids:
    print(f"Inserting {user_id}")
    bst.insert(user_id)

# Print the BST in sorted order
print("\nBST values in sorted order (inorder traversal):")
print(bst.inorder_traversal())

# Let's visualize the tree structure
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level * 4 + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

print("\nBST Structure:")
print_tree(bst.root)

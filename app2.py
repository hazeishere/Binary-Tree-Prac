class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def find_lca(self, p, q):
        """
        Find the lowest common ancestor of two nodes p and q
        
        Args:
            p: first node value
            q: second node value
            
        Returns:
            The value of the lowest common ancestor node, or None if not found
        """
        if not self.root:
            return None
            
        result = self._find_lca_recursive(self.root, p, q)
        return result.val if result else None
    
    def _find_lca_recursive(self, node, p, q):
        """
        Helper method to recursively find LCA of two nodes
        
        Args:
            node: current node being examined
            p: first node value to find
            q: second node value to find
            
        Returns:
            The LCA node if found, None otherwise
        """
        # Base case: if node is None, return None
        if not node:
            return None
            
        # If current node is one of the targets, return it
        if node.val == p or node.val == q:
            return node
            
        # Look for the nodes in left and right subtrees
        left_lca = self._find_lca_recursive(node.left, p, q)
        right_lca = self._find_lca_recursive(node.right, p, q)
        
        # If both left and right subtrees return a node, current node is the LCA
        if left_lca and right_lca:
            return node
            
        # Otherwise, return the non-None value (if any)
        return left_lca if left_lca else right_lca
    
    def insert(self, values, root=None, index=0):
        """
        Insert nodes level by level based on a list of values.
        This method builds a complete binary tree.
        
        Args:
            values: List of values to insert
            root: Current root node (used for recursion)
            index: Current index in the list (used for recursion)
            
        Returns:
            The root node of the subtree
        """
        if not values:
            return None
            
        if index < len(values):
            if values[index] is None:
                return None
                
            # Create a new node with the current value
            node = TreeNode(values[index])
            
            # Recursively build left and right subtrees
            node.left = self.insert(values, node.left, 2 * index + 1)
            node.right = self.insert(values, node.right, 2 * index + 2)
            
            return node
        
        return None
    
    def build_tree(self, values):
        """
        Build a tree from a list of values
        
        Args:
            values: List of values to build the tree
        """
        self.root = self.insert(values)
        
    def print_tree(self):
        """Print the tree in an inorder traversal"""
        result = []
        self._inorder_traversal(self.root, result)
        return result
        
    def _inorder_traversal(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)


def main():
    # Example usage
    tree = BinaryTree()
    
    # Build a sample tree:
    #       3
    #      / \
    #     5   1
    #    / \  / \
    #   6  2  0  8
    #     / \
    #    7   4
    
    tree.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    
    # Find LCA of nodes with values 5 and 1 (should be 3)
    lca1 = tree.find_lca(5, 1)
    print(f"LCA of 5 and 1: {lca1}")  # Expected: 3
    
    # Find LCA of nodes with values 5 and 4 (should be 5)
    lca2 = tree.find_lca(5, 4)
    print(f"LCA of 5 and 4: {lca2}")  # Expected: 5
    
    # Find LCA of nodes with values 6 and 4 (should be 5)
    lca3 = tree.find_lca(6, 4)
    print(f"LCA of 6 and 4: {lca3}")  # Expected: 5


if __name__ == "__main__":
    main()

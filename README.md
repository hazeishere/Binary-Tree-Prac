# Binary Tree Contact Manager

This project implements a Binary Search Tree (BST) to manage contacts efficiently.

## What is a Binary Tree?

A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. In this project, we've implemented a specific type of binary tree called a Binary Search Tree (BST).

## How Binary Search Trees Work

In a BST:
- Each node contains a key (in our case, a contact name) and associated data
- For any given node:
  - All nodes in its left subtree have keys less than the node's key
  - All nodes in its right subtree have keys greater than the node's key
- This ordering property enables efficient searching, insertion, and deletion operations

## Why Binary Search Trees are Effective

BSTs provide an excellent balance of efficiency for several operations:
- Search operations are fast (O(log n) average case) because each comparison eliminates roughly half of the remaining tree
- Insertions and deletions maintain the tree's ordering property while being reasonably efficient
- The data is kept sorted, allowing for operations like retrieving contacts in alphabetical order

## Use Cases for Binary Search Trees

Binary Search Trees are ideal for:
1. **Dictionary implementations** - Fast lookup by key
2. **Database indexing** - Efficient data retrieval
3. **Symbol tables** in compilers
4. **Contact management systems** (like this project)
5. **Priority queues**

## Our Contact Manager Implementation

This project demonstrates a contact management system using a BST where:
- Contacts are stored with name and phone number
- Contacts are organized by name in the tree
- The implementation supports:
  - Adding new contacts
  - Finding contacts by name
  - Deleting contacts
  - Listing all contacts in alphabetical order

## Lowest Common Ancestor (LCA) Finder

The project now includes a binary tree implementation with functionality to find the Lowest Common Ancestor (LCA) of two nodes.

### What is a Lowest Common Ancestor?

The Lowest Common Ancestor of two nodes in a tree is the deepest node that has both nodes as descendants. A node can be a descendant of itself.

### How LCA Finding Works

The algorithm uses a recursive approach:
1. If the current node is null, return null
2. If the current node matches either of the target nodes, return the current node
3. Recursively search for the nodes in left and right subtrees
4. If both left and right subtree searches return non-null values, the current node is the LCA
5. Otherwise, return the non-null result from either subtree

### Time and Space Complexity

- **Time Complexity**: O(n) where n is the number of nodes in the tree
- **Space Complexity**: O(h) where h is the height of the tree (for the recursion stack)

### Usage Example

The implementation is available in `app2.py`:

```python
from app2 import BinaryTree

# Create a binary tree
tree = BinaryTree()

# Build a tree from a list of values
tree.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

# Find the LCA of nodes with values 5 and 1
lca = tree.find_lca(5, 1)  # Returns 3
```

## Getting Started

To use the contact manager:

```python
from app import Contact, ContactManager

# Create a new contact manager
manager = ContactManager()

# Add contacts
manager.add_contact(Contact("Alice", "123-456-7890"))
manager.add_contact(Contact("Bob", "234-567-8901"))

# Find a contact
contact = manager.find_contact("Alice")

# List all contacts in alphabetical order
all_contacts = manager.list_all_contacts()

# Delete a contact
manager.delete_contact("Alice")
```

## Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insert    | O(log n)     | O(n)       |
| Delete    | O(log n)     | O(n)       |

Note: The worst case O(n) occurs in unbalanced trees. For better performance in all cases, balanced BST variants like AVL trees or Red-Black trees can be used. 
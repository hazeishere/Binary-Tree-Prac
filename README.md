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
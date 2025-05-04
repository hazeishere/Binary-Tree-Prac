class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name}: {self.phone}"


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None


class ContactManager:
    def __init__(self):
        self.root = None
    
    def add_contact(self, contact):
        """Add a new contact to the BST"""
        if self.root is None:
            self.root = Node(contact)
            return True
        
        return self._add_contact_recursive(self.root, contact)
    
    def _add_contact_recursive(self, current_node, contact):
        """Helper method to recursively add a contact to the BST"""
        # Compare names for BST ordering
        if contact.name < current_node.contact.name:
            if current_node.left is None:
                current_node.left = Node(contact)
                return True
            return self._add_contact_recursive(current_node.left, contact)
        elif contact.name > current_node.contact.name:
            if current_node.right is None:
                current_node.right = Node(contact)
                return True
            return self._add_contact_recursive(current_node.right, contact)
        else:
            # Contact with same name already exists
            return False
    
    def find_contact(self, name):
        """Find a contact by name"""
        return self._find_contact_recursive(self.root, name)
    
    def _find_contact_recursive(self, current_node, name):
        """Helper method to recursively find a contact by name"""
        if current_node is None:
            return None
        
        if name == current_node.contact.name:
            return current_node.contact
        elif name < current_node.contact.name:
            return self._find_contact_recursive(current_node.left, name)
        else:
            return self._find_contact_recursive(current_node.right, name)
    
    def delete_contact(self, name):
        """Delete a contact by name"""
        self.root, deleted = self._delete_contact_recursive(self.root, name)
        return deleted
    
    def _delete_contact_recursive(self, current_node, name):
        """Helper method to recursively delete a contact"""
        if current_node is None:
            return None, False
        
        if name < current_node.contact.name:
            current_node.left, deleted = self._delete_contact_recursive(current_node.left, name)
            return current_node, deleted
        elif name > current_node.contact.name:
            current_node.right, deleted = self._delete_contact_recursive(current_node.right, name)
            return current_node, deleted
        else:
            # Node to delete found
            
            # Case 1: Node with no children
            if current_node.left is None and current_node.right is None:
                return None, True
            
            # Case 2: Node with only one child
            elif current_node.left is None:
                return current_node.right, True
            elif current_node.right is None:
                return current_node.left, True
            
            # Case 3: Node with two children
            else:
                # Find the smallest value in the right subtree
                successor = self._find_min(current_node.right)
                current_node.contact = successor.contact
                # Delete the successor
                current_node.right, _ = self._delete_contact_recursive(current_node.right, successor.contact.name)
                return current_node, True
    
    def _find_min(self, node):
        """Find the leftmost node (minimum value)"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def list_all_contacts(self):
        """List all contacts in alphabetical order"""
        contacts = []
        self._inorder_traversal(self.root, contacts)
        return contacts
    
    def _inorder_traversal(self, node, contacts):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_traversal(node.left, contacts)
            contacts.append(node.contact)
            self._inorder_traversal(node.right, contacts)


# Example usage
def main():
    contact_manager = ContactManager()
    
    # Add some contacts
    contact_manager.add_contact(Contact("Alice", "123-456-7890"))
    contact_manager.add_contact(Contact("Bob", "234-567-8901"))
    contact_manager.add_contact(Contact("Charlie", "345-678-9012"))
    contact_manager.add_contact(Contact("David", "456-789-0123"))
    
    # Find a contact
    contact = contact_manager.find_contact("Bob")
    if contact:
        print(f"Found contact: {contact}")
    else:
        print("Contact not found")
    
    # List all contacts
    print("\nAll contacts:")
    for contact in contact_manager.list_all_contacts():
        print(contact)
    
    # Delete a contact
    if contact_manager.delete_contact("Charlie"):
        print("\nDeleted Charlie successfully")
    else:
        print('\n error message')

    # List all contacts after deletion
    print("\nContacts after deletion:")
    for contact in contact_manager.list_all_contacts():
        print(contact)


if __name__ == "__main__":
    main()

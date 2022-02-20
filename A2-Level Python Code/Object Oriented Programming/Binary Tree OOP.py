# Binary Tree OOP.py
# Initialize new binary tree
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    # Procedure to add item to binary tree - recursive solution
    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item

    # Function to search for item in binary tree
    def search(self, item):
        while self.item != item:
            if item < self.item:
                self.item = self.left
            else:
                self.item = self.right
            
            if self.item is None:
                return None
        
        return self.item

    def showDetails(self):
        print(self)



# Initialize new tree with class Node
tree = Node(27)

# Execute addition procedures
tree.insert(19)
tree.insert(36)
tree.insert(42)
tree.insert(16)

# Execute search function - returning the place of the found item
tree.search(36)
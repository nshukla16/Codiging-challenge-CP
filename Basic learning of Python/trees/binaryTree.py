class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

        

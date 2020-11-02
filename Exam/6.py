def printTree(tree):
   if tree == None: return
   printTree(tree.left)
   print(tree.cargo, end = " ")
   printTree(tree.right)

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left 
        self.right = right
        
    def __str__(self):
        return str(self.cargo)


tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
printTree(tree)
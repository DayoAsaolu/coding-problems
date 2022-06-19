class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"  {self.val} --> [{self.left} {self.right}]"
            

def preorderTraversal(root):
    if not root: return []
    
    elements = []
    treeStack = [root]
    
    while len(treeStack) != 0:
        curr = treeStack.pop()
        elements.append(curr.val)
        
        if curr.right: treeStack.append(curr.right)
        if curr.left:  treeStack.append(curr.left)
            
            
    return elements


def inorderTraversal(root):
    if not root: return []
    
    elements = []
    
    
   
            
            
    return elements
def main():
    """
                    1
                    
            2               5

        3       4       6       7
    """
    """
                    F
                    
            B               G


        A       D               I

             C     E          H   
    """
    # numbers
    l = TreeNode(2, TreeNode(3), TreeNode(4))
    r = TreeNode(5, TreeNode(6), TreeNode(7))
    h = TreeNode(1, l, r)

    # print(h)
    # print(preorderTraversal(h))

    # letters
    l = TreeNode("B", TreeNode("A"), TreeNode("D", TreeNode("C"), TreeNode("E")))
    r = TreeNode("G",None, TreeNode("I", TreeNode("H")))
    h = TreeNode("F", l, r)

    print(h)
    return 0


main()
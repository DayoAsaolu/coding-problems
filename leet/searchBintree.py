import re


class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val} -> [{self.left}, {self.right}]"

def searchBST(root, val):
    if root.val == val or root == None: return root

    if root.left:
        return searchBST(root.left, val)

    if root.right:
        return searchBST(root.right, val)

def BSTsearch(root, val):
    if root.val == val:
        return root
    
    if root == None:
        return root

    treeStack = [ root ]
    while len(treeStack) != 0:
        curr = treeStack.pop()
        if curr.val == val:
            return curr
        else:
            if curr.left is not None: treeStack.append(curr.left) 
            if curr.right is not None: treeStack.append(curr.right)

    return None

def main():
    child = TreeNode(2, TreeNode(1), TreeNode(3))
    head = TreeNode(4,child, TreeNode(7))
    print("tree: ", head)

    # print("ans---> ", searchBST(head, 5))
    print("ans---> ", BSTsearch(head, 2))

    return 0


main()
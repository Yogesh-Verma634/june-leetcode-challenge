class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InvertBT:

    # def __init__(self, root):
    #     self.root = root

    def invertBinaryTree(self, root):

        def helper(root):
            if not root:
                return None
            
            left = root.left
            right = root.right

            root.left, root.right = right, left

            helper(left)
            helper(right)
            return root
        
        return helper(root)

'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9
'''
if __name__ == "__main__":

    def printInorder(root):
        if root:
            printInorder(root.left)
            print(root.val)
            printInorder(root.right)

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    invertbt = InvertBT()
    invertedRoot = invertbt.invertBinaryTree(root)
    printInorder(invertedRoot)
    

    

        
class Solution:
    
    def height(self, root):
        if root is None:
            return 0
        leftHeight=self.height(root.left)
        if leftHeight is None:
            return None
        rightHeight=self.height(root.right)
        if rightHeight is None or abs(leftHeight - rightHeight) > 1:
            return None
        return max(leftHeight,rightHeight)+1
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.height(root)!=None
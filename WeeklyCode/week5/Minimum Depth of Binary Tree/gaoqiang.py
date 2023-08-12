# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        height = 1
        while queue:
            tmpList = []
            while queue:
                tmpList.append(queue.pop(0))
            for i in range(0,len(tmpList)):
                tmpNode = tmpList[i]
                if tmpNode.left is None and tmpNode.right is None:
                    return height
                if tmpNode.left!=None:
                	queue.append(tmpNode.left)
                if tmpNode.right!=None:
                	queue.append(tmpNode.right)
            height = height+1

if __name__=='__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left = TreeNode(3)       
	s = Solution()
	print s.minDepth(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Store the max as we go down
        def dfs(node, curMax):
            if not node:
                return 0

            newMax = max(curMax, node.val)
            goodNodes = dfs(node.left, newMax) + dfs(node.right, newMax)
            if node.val >= curMax:
                goodNodes += 1

            return goodNodes
        
        return dfs(root, root.val)
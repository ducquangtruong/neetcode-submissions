# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Return the max sum containing the node
        def dfs(node):
            if not node:
                return [-float("infinity"), 0]
            maxLeftA, maxLeftB = dfs(node.left)
            maxRightA, maxRightB = dfs(node.right)
            maxContainingNode = max(maxLeftB + node.val, maxRightB + node.val, node.val)
            return [
                max(maxLeftA, maxRightA, maxContainingNode, maxLeftB + maxRightB + node.val, node.val),
                maxContainingNode
            ]
        
        return dfs(root)[0]
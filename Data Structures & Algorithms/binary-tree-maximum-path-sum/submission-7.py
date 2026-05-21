# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Idea: Compare max to root.val + maxLeft + maxRight
        def dfs(root):
            if not root:
                return (float("-inf"), float("-inf"))
            maxOverallLeft, maxPathLeft = dfs(root.left)
            maxOverallRight, maxPathRight = dfs(root.right)
            # Ignore negative paths
            maxPathLeft = max(0, maxPathLeft)
            maxPathRight = max(0, maxPathRight)
            maxOverall = max(
                maxOverallLeft, maxOverallRight,
                maxPathLeft + maxPathRight + root.val
            )
            maxPath = max(maxPathLeft, maxPathRight) + root.val
            return (maxOverall, maxPath)
        
        return dfs(root)[0]
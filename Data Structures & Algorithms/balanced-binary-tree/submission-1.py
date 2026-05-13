# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return (isBalanced, height)
        def dfs(root):
            if not root:
                return [True, 0]
            
            isBalancedLeft, leftHeight = dfs(root.left)
            isBalancedRight, rightHeight = dfs(root.right)

            return [
                isBalancedLeft and isBalancedRight and abs(leftHeight - rightHeight) < 2,
                1 + max(leftHeight, rightHeight)
            ]
        
        return dfs(root)[0]
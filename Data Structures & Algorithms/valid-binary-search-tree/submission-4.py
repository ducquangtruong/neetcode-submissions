# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Return (isValid, min, max)
        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"))

            leftValid, leftMin, leftMax = dfs(node.left)
            rightValid, rightMin, rightMax = dfs(node.right)

            valid = leftValid and rightValid and leftMax < node.val < rightMin
            minVal = min(leftMin, rightMin, node.val)
            maxVal = max(leftMax, rightMax, node.val)

            return (valid, minVal, maxVal)
        
        return dfs(root)[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Return the min/max value of the tree
        def DFS(root):
            if not root:
                return [float("infinity"), -float("infinity"), True]
            minLeft, maxLeft, resLeft = DFS(root.left)
            minRight, maxRight, resRight = DFS(root.right)
            maxVal = max(maxLeft, maxRight, root.val)
            minVal = min(minLeft, minRight, root.val)
            if maxLeft >= root.val or minRight <= root.val:
                return [minVal, maxVal, False]
            return [minVal, maxVal, resLeft and resRight]
        
        return DFS(root)[2]
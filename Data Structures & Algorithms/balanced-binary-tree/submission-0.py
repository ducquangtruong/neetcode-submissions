# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        isTreeBalanced = True
        
        def DFS(node):
            nonlocal isTreeBalanced
            if node is None:
                return 0
            
            left = DFS(node.left)
            right = DFS(node.right)
            if abs(left - right) > 1:
                isTreeBalanced = False
            return max(left, right) + 1
        
        DFS(root)
        return isTreeBalanced
                
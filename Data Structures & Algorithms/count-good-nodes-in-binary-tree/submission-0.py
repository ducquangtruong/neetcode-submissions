# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(node, maximum):
            if not node:
                return 0
            good = 0
            if node.val >= maximum:
                good += 1
            good += DFS(node.left, max(node.val, maximum))
            good += DFS(node.right, max(node.val, maximum))
            return good
        
        return DFS(root, -float("infinity"))
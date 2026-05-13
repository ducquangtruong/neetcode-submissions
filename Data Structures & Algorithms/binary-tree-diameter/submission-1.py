# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative solution
        # Node: (height, diameter)
        data = {None: (0, 0)}
        stack = [root]

        while stack:
            node = stack[-1]
            if node.left and node.left not in data:
                stack.append(node.left)
            elif node.right and node.right not in data:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = data[node.left]
                rightHeight, rightDiameter = data[node.right]

                data[node] = (
                    1 + max(leftHeight, rightHeight),
                    max(leftHeight + rightHeight, leftDiameter, rightDiameter)
                )
        
        return data[root][1]

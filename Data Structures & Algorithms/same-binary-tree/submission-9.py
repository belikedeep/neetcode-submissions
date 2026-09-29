from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p,q)])

        while queue:
            l_node, r_node = queue.popleft()

            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None:
                return False
            if l_node.val != r_node.val:
                return False
            
            queue.append((l_node.left, r_node.left))
            queue.append((l_node.right, r_node.right))

        return True







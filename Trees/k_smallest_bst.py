# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in order traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # no of visited nodes
        stack = []
        cur = root # node currently visiting

        while cur and stack:
            # to the left most val = min
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
                
            # explore right
            cur = cur.right
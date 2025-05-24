# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # bottom up dfs
        def dfs(root):
            if not root:
                return [True, 0] # [isbalanced, height]

            left, right = dfs(root.left), dfs(root.right) # dfs left, right to bottom
            # check if left and right balanced
            # then check if h_left - h_right <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) 
            
            return [balanced, 1 + max(left[1], right[1])] # return [isbalanced, height] for each node

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # for learning purposes
    # iterative bfs
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        level = 0
        queue = deque([root])
        while queue:
            for i in range(len(q)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1
        return level
    
    # iterative iterative dfs 
    # (preorder because its easiest for this problem => adding parent then children)
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
            if node: # null check
                res = max(res, depth)
                # preorder -> root, left, right
                stack.extend([node.left, depth + 1]) # might add null nodes, thus the check
                stack.extend([node.right, depth + 1])  
        return res
                
    
    

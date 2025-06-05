# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node, left, right
        # inorder = left, node, right
        
        # base case: if either list is empty, there's no tree to build
        if not preorder or not inorder:
            return None

        # first element of preorder is the root
        root = TreeNode(preorder[0]) 

        # find the root in inorder to determine the left and right subtrees 
        # elements to the left of 'mid' in inorder are in the left subtree
        # elements to the right of 'mid' in inorder are in the right subtree
        mid = inorder.index(root.val) 
        
        # the number of elements on the left/right (from inorder) tells us how to split preorder 
        # for left child => split preorder from element after root to number of elements in left subtree (mid),
        # and take only the elements before mid (root, taking the left subtree) from inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # for right child => split preorder from mid + 1 (start of right half) to the end,
        # and take only the elements after mid (root, taking the right) from inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

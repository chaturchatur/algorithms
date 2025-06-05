# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) solution
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
        mid = inorder.index(root.val)  # O(n) to search
        
        # O(n) for recursion
        # the number of elements on the left/right (from inorder) tells us how to split preorder 
        # for left child => split preorder from element after root to number of elements in left subtree (mid),
        # and take only the elements before mid (root, taking the left subtree) from inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # for right child => split preorder from mid + 1 (start of right half) to the end,
        # and take only the elements after mid (root, taking the right) from inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

    # O(n) solution w/ hashmap optimization
    # Definition for a binary tree node.

    def buildTreeHashMap(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hashmap for fast lookup for inorder indexes - search is now O(1)
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0 # track preorder index
        # recursive dfs
        def dfs(l, r):
            # base case: if l > r, then we've traversed through all elements
            if l > r: 
                return None

            # root is the first element of preorder 
            # increment preorder index for next iteration after picking root val
            # creating the root as a treenode
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1 
            root = TreeNode(root_val)
            
            # finding the mid point index in inorder
            # all elements to the left of mid in inorder (l to mid - 1) are in the left subtree
            # all elements to the right of mid in inorder (mid + 1 to r) are in the right subtree
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root

        return dfs(0, len(inorder) - 1) 
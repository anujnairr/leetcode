# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
root = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        def dfs(node):
            if (not node):
                return

            nonlocal curSum

            dfs(node.right)
            node.val += curSum
            curSum = node.val
            dfs(node.left)
        dfs(root)
        return root

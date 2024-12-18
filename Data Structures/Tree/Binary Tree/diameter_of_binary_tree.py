# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.res = max(self.res, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.res

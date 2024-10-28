# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
root = [], targetSum = 0
root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):

        def dfs(node, curSum):
            if node is None:
                return False

            curSum += node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
                else:
                    return False
            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)

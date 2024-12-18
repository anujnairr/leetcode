# # Given the root of a binary tree, return all root-to-leaf paths in any order.
# # A leaf is a node with no children.
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        self.ans = []

        def dfs(node, temp):
            if not node:
                return
            temp += str(node.val) + "->"
            if not node.left and not node.right:
                self.ans.append(temp[:len(temp)-2])

            dfs(node.left, temp)
            dfs(node.right, temp)

        dfs(root, "")
        return self.ans

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):

        self.hashmap = {}

        def dfs(node):
            if not node:
                return
            if node.val in self.hashmap:
                self.hashmap[node.val] += 1
            else:
                self.hashmap[node.val] = 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        if not root.left and not root.right:
            return [root.val]

        maximum = max(self.hashmap.values())
        arr = []
        for i, j in self.hashmap.items():
            if j == maximum:
                arr.append(i)
        return arr

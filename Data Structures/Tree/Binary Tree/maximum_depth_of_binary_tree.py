# # Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = [3, 9, 20, null, null, 15, 7]


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive Depth First Search (DFS)
        # if not root:
        #     return 0

        # res = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # return res

        # Breadth First Search (BFS) without recursion
        # if not root:
        #   return 0
        # queue = deque([root])
        # level = 0
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        # return level

        # Iterative DFS
        stack = [root, 1]
        res = 0
        while stack:
            node, depth = stack.pop()
            res = max(depth, res)
            if node:
                stack.append(node.left, depth + 1)
                stack.append(node.right, depth + 1)

        return depth

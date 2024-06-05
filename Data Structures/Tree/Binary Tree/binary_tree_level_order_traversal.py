# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

from collections import deque
root = [3, 9, 20, null, null, 15, 7]

res = []
queue = deque([root])

while queue:
    temparr = []
    for i in range(len(queue)):
        node = queue.popleft()
        temparr.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    res.append(temparr)

print(res)

# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.

head = [5, 2, 13, 3, 8]

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


stack = []

itr = head
while itr:
    while stack and itr.val > stack[-1]:
        stack.pop()
    stack.append(itr.val)
    itr = itr.next

dummy = ListNode()
cur = dummy
for n in stack:
    newnode = ListNode(n)
    cur.next = newnode
    cur = cur.next

return dummy.next

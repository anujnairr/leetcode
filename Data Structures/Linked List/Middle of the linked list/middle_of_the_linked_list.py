# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
head = [1, 2, 3, 4, 5]

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):

        left, right = head, head
        while right and right.next:
            left = left.next
            right = right.next.next
        return left

# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

head = [1, 2, 3, 4, 5]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        p = None
        c = head
        while c:
            t = c.next
            c.next = p
            p = c
            c = t

        return p

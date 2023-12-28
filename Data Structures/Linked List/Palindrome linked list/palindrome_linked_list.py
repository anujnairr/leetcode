# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

head = [1, 2, 2, 1]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        itr = head
        # left and right pointers
        left, right = itr, itr

        # right is true and until right.next reaches None
        while right and right.next is not None:
            left = left.next
            right = right.next.next

        # 1 -> 2 -> 2 -> 1
        p = None
        c = left
        while c:
            t = c.next
            c.next = p
            p = c
            c = t

        left = p
        while left:
            if left.val != head.val:
                return False
            left = left.next
            head = head.next
        return True
        # Solution involving array and left/right pointer.
        # itr = head
        # arr = []
        # while itr is not None:
        #     arr.append(itr.value)
        #     itr = itr.next

        # left = 0
        # right = len(arr) - 1

        # while left <= right:
        #     if arr[left] != arr[right]:
        #         return False
        # return True

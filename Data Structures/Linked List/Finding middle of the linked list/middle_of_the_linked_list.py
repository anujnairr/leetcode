# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.head = None

    def insertion_at_beginning(self, data):
        node1 = ListNode(data, self.head)
        self.head = node1

    def insertion_at_end(self, data):
        if self.head == None:
            node1 = ListNode(data)
            self.head = node1
        else:
            itr = self.head
            while itr:
                if itr.next == None:
                    node1 = ListNode(data)
                    itr.next = node1
                    break
                itr = itr.next

    def traversing(self):
        itr = self.head
        while itr:
            print(f"{itr.val}")
            itr = itr.next

    def count(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1

        return count

    def middleNode(self):
        itr = self.head
        # while itr:
        #     array.append(itr.val)
        #     itr = itr.next
        # middle = int((len(array))/2 + 1)
        # print(middle)
        # for i in range(middle-1, len(array)):
        #     (array[i])
        count = self.count()
        middle = int((count/2) + 1)
        c = 1
        while itr:

            if middle == c:
                self.head = itr
                break
            c += 1
            itr = itr.next


data = Solution()
data.insertion_at_end(10)
data.insertion_at_end(20)
data.insertion_at_end(30)
data.insertion_at_end(40)
data.insertion_at_end(50)
data.insertion_at_end(60)
# data.insertion_at_end(70)
# data.traversing()
# print(data.count())
data.middleNode()
data.traversing()

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            raise Exception("No Linked List")

        itr = self.head
        while itr:
            print(f"{itr.val}-->", end="")
            itr = itr.next

    def insert_at_beginning(self, val):
        node1 = ListNode(val, self.head)
        self.head = node1

    def reverse_linkedlist(self):
        ls = Linked_List()
        itr = self.head

        while itr:
            node2 = ListNode(itr.val, ls.head)
            # print(node2.val)
            ls.head = node2
            itr = itr.next

        ls.traversal()


ll = Linked_List()


ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
# ll.traversal()
ll.reverse_linkedlist()

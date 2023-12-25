# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Node:
    def __init__(self, data=0, next=None):
        self.value = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node1 = Node(data, self.head)
        self.head = node1

    def print_list(self):
        if self.head == None:
            print("List is empty")

        ll_print = ""
        itr = self.head
        while itr:
            ll_print += str(itr.value) + "-->"
            itr = itr.next
        print(ll_print)

    def insert_at_end(self, data):
        if self.head == None:
            print("List is empty")
        itr = self.head
        while itr:
            if itr.next == None:
                end_node = Node(data)
                itr.next = end_node
                break
            itr = itr.next

    def get_length_of_list(self):
        if self.head == None:
            print("List is empty")
        count = 0
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next
        print(f"The length of list is: {count}")

    def add_node_at_specific_index(self, index, data):
        if self.head == None:
            print("List is empty.")
        itr = self.head
        count = 0
        # edge case of adding node at first position (self.head)
        if index == count:
            node1 = Node(data, self.head)
            self.head = node1
            return
        while itr is not None:
            if count == index-1:
                node1 = Node(data, itr.next)
                itr.next = node1
                break
            itr = itr.next
            count += 1

    def remove_node_at_specific_index(self, index):
        if self.head == None:
            print("List is empty")
        count = 0
        itr = self.head
        # edge case of removing self.head
        if count == index:
            self.head = itr.next

        while itr != None:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_after_specific_value(self, insert_data, after_data):
        if self.head == None:
            print("This list is empty")
        itr = self.head
        while itr is not None:
            if after_data == itr.value:
                node1 = Node(insert_data, itr.next)
                itr.next = node1
            itr = itr.next

    def remove_after_specific_value(self, after_data):
        if self.head == None:
            print("List is empty")
        itr = self.head
        while itr is not None:
            if after_data == itr.value:
                itr.next = itr.next.next
            itr = itr.next

    def remove_by_value(self, remove_value):
        if self.head == None:
            print("This list is empty")
        itr = self.head
        # edge case of removing self.head
        if remove_value == itr.value:
            self.head = itr.next
            return
        while itr is not None:
            temp = itr.next
            if remove_value == temp.value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def middle_of_linked_list(self):
        if self.head == None:
            print("List is empty")
            return
        itr = self.head
        count = 0
        arr = []
        while itr is not None:
            count += 1
            arr.append(itr.value)
            itr = itr.next

        middle = int(count/2)
        print(arr[middle])


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(2)
    ll.insert_at_begin(1)
    ll.insert_at_end(3)
    ll.print_list()
    ll.get_length_of_list()
    ll.add_node_at_specific_index(2, 0)
    ll.insert_at_end(4)
    ll.print_list()
    ll.remove_node_at_specific_index(3)
    ll.print_list()
    ll.insert_after_specific_value(10, 2)
    ll.print_list()
    ll.remove_after_specific_value(0)
    ll.print_list()
    ll.remove_by_value(10)
    ll.print_list()
    ll.add_node_at_specific_index(0, 9)
    ll.print_list()
    ll.remove_node_at_specific_index(0)
    ll.print_list()
    ll.middle_of_linked_list()

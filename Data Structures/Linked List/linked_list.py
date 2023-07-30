class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node1 = Node(data, self.head)
        self.head = node1

    def traversing(self):
        if self.head is None:
            print("Illa")
        else:
            itr = self.head
            while itr is not None:
                print(f"{itr.data}-->")
                itr = itr.next

    def get_the_motherfucking_length(self):
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr != None:
                count += 1
                itr = itr.next
        return count

    def add_node_at_the_motherfucking_index(self, index, data):
        count = 1
        if index < 0 or index > self.get_the_motherfucking_length():
            print("Motherfucker, give a valid index, please, for fuck's sake.")
        else:
            itr = self.head
            while itr is not None:
                itr = itr.next
                count += 1
                if count == index-1:
                    node1 = Node(data, itr.next)
                    itr.next = node1
                    break

    def insert_at_end(self, data):
        if self.head is None:
            raise Exception("Sadanam kaiyil illa")
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            node1 = Node(data)
            itr.next = node1

    def remove_node_at_motherfucking_index(self, index):
        count = 1
        if index < 0 or index > self.get_the_motherfucking_length():
            raise Exception("Myre, nere chovve index thaa")
        else:
            itr = self.head
            while count != index - 1:
                itr = itr.next
                count += 1
            itr.next = itr.next.next

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr is not None:
            if itr.data == data_after:
                node1 = Node(data_to_insert, itr.next)
                itr.next = node1

            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        if self.head is None:
            raise Exception("Linked list is empty")
        else:
            while itr is not None:
                if itr.data == data:
                    self.head = itr.next
                    break
                else:
                    next_node = itr.next
                    if next_node.data == data:
                        itr.next = itr.next.next
                        break
                itr = itr.next


linked_list = LinkedList()
linked_list.insert_at_beginning(60)
linked_list.insert_at_beginning(50)
linked_list.insert_at_beginning(40)
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(10)
# print(linked_list.get_the_motherfucking_length())
# linked_list.add_node_at_the_motherfucking_index(3, 1000)
# linked_list.traversing()
# linked_list.insert_at_end(20)
# linked_list.remove_node_at_motherfucking_index(3)
# linked_list.traversing()
# linked_list.insert_after_value(40, 100)
# linked_list.traversing()
linked_list.remove_by_value(10)
linked_list.traversing()

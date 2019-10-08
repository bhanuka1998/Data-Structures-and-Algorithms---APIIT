class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def insert_front(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def insert_end(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def insert_middle(self, new_node, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                break
            current_node = current_node.next_node
        if current_node:
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
        else:
            print("No such value")

    def delete_node(self, value):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == value:
                print("To be deleted", current_node.data)
                break
            # current_node = current_node.next_node
            previous_node = current_node
            current_node = current_node.next_node
        if previous_node == None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node
        if current_node.next_node == None:
            self.tail = previous_node
        else:
            print("There is no list")
        # print(previous_node.data)


list_1 = LinkedList()
list_1.insert_front(Node(data=5))
list_1.insert_front(Node(data=3))
list_1.insert_end(Node(data=8))
list_1.insert_middle(Node(data=4), 5)
list_1.insert_middle(Node(data=7), 4)
list_1.insert_middle(Node(data=90), 4)
list_1.insert_middle(Node(data=7), 80)
list_1.delete_node(value=5)
list_1.traverse()
print(list_1.is_empty())

class Stack:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def push(self, new_node=None):
        new_node.next_node = self.head
        self.head = new_node

    def pop(self,):
        if not self.is_empty():
            current_data = self.head.data
            self.head = self.head.next_node
            return current_data
        else:
            print("Stack is empty")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.head.data)


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


stack_1 = Stack()
node_1 = Node()
stack_1.push(Node(data=12))
stack_1.push(Node(data=13))
stack_1.push(Node(data=14))
print(stack_1.pop())
stack_1.push(Node(data=15))
stack_1.peek()
# print(stack_1.pop())
print(stack_1.is_empty())

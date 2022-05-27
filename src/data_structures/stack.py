from data_structures.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value: int):
        self.linked_list.append_left(value)

    def pop(self) -> int:
        return self.linked_list.pop_left()

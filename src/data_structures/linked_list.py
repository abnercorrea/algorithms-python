from typing import List


class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, values: List[int] = None):
        self.left = None
        self.right = None

        for value in values or []:
            self.append(value)

    def append_left(self, value: int):
        self.left = LinkedListNode(value, self.left)
        if not self.right:
            self.right = self.left

    def append(self, value: int):
        if self.right:
            self.right.next = LinkedListNode(value)
            self.right = self.right.next
        else:
            self.right = self.left = LinkedListNode(value)

    def pop_left(self) -> int:
        if not self.left:
            return None
        value = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return value

    def empty(self) -> bool:
        return self.left is None

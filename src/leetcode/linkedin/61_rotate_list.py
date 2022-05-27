import pytest

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_size_and_tail(head: Optional[ListNode]) -> int:
    size = 0
    node, prev = head, None

    while node:
        size += 1
        prev = node
        node = node.next

    return size, prev


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    size, tail = list_size_and_tail(head)
    k = k % size

    if k == 0:
        return head

    axis, new_tail = head, None
    for _ in range(size - k):
        new_tail = axis
        axis = axis.next

    new_tail.next = None
    tail.next = head

    return axis


def linked_list_to_array(head: Optional[ListNode]):
    array = []
    node = head
    while node:
        array.append(node.val)
        node = node.next
    return array


def array_to_linked_list(arr: List[int]):
    if not arr:
        return
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head


def test_rotate_right():
    l = array_to_linked_list(list(range(10)))
    assert linked_list_to_array(rotate_right(l, 1)) == [9,0,1,2,3,4,5,6,7,8]
    l = array_to_linked_list(list(range(10)))
    assert linked_list_to_array(rotate_right(l, 10)) == [0,1,2,3,4,5,6,7,8,9]


if __name__ == '__main__':
    pytest.main()

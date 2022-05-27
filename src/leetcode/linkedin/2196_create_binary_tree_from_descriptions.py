import pytest
from collections import deque
from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(parent: int, parent_child: Dict[int, List[TreeNode]]) -> TreeNode:
    if not parent:
        return None
    node = TreeNode(parent)
    children = parent_child.get(parent)
    if children:
        node.left = build_binary_tree(children[1], parent_child)
        node.right = build_binary_tree(children[0], parent_child)
    return node


def create_binary_tree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    parent_child = {}
    children = set()
    for parent, child, is_left in descriptions:
        if parent not in parent_child:
            parent_child[parent] = [None, None]
        parent_child[parent][is_left] = child
        children.add(child)
    root_val = None
    for parent in parent_child:
        if parent not in children:
            root_val = parent
            break
    root = build_binary_tree(root_val, parent_child)
    return root


def traverse_tree(root: TreeNode, order: str) -> List[int]:
    result = []
    if order == 'inorder':
        inorder(root, result)
    elif order == 'preorder':
        preorder(root, result)
    elif order == 'postorder':
        postorder(root, result)
    return result


def inorder(node: TreeNode, result: List[int]):
    if not node:
        return
    inorder(node.left)
    result.append(node.val)
    inorder(node.right)


def preorder(node: TreeNode, result: List[int]):
    if not node:
        return
    result.append(node.val)
    preorder(node.left)
    preorder(node.right)


def postorder(node: TreeNode, result: List[int]):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    result.append(node.val)


def level_order(root: TreeNode) -> List[int]:
    result = []
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
    return result


def test_create_binary_tree():
    assert inorder(create_binary_tree([[100,200,1]])) == [200, 100]
    assert inorder(create_binary_tree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])) == [15,20,17,50,19,80]
    assert preorder(create_binary_tree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])) == [50,20,15,17,80,19]
    assert level_order(create_binary_tree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])) == [50,20,80,15,17,19]


if __name__ == '__main__':
    pytest.main()

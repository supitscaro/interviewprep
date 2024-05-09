"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

"""


def recursiveInorderTraversal(root):
    result = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    return result


def iterativeInorderTraversal(root):
    if not root:
        return

    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)

        current = current.right

    return result

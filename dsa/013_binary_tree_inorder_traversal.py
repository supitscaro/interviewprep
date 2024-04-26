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

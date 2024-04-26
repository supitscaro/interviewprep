"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""


def preorderTraversal(root):
    result = []

    def preorder(root):
        if not root:
            return

        result.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)

    return result

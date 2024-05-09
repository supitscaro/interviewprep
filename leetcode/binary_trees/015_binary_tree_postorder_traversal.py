"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

"""


def postOrderTraversal(root):
    result = []

    def postorder(root):
        if not root:
            return

        postorder(root.left)
        postorder(root.right)
        result.append(root.val)

    postorder(root)

    return result

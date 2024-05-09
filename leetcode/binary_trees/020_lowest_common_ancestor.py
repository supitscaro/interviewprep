"""
Given a binary search tree (BST), find the lowest common
ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The
lowest common ancestor is defined between two nodes p
and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant
of itself).”


Notes:
a binary search tree will have a right subtree node that has a
value greater than the parent node value. It will also have a
subtree whose node will be less than the parent node.

if p or q is less than root.val, then we can go to the left
node.
if p or q is greater than root.val, then we can go to the
right node
if one is less than root.val and if one is greater than
root.val, then the current node is the lowest common ancestor

"""

# Time complexity: O(n) where n is the height of the tree
# Space complexity: O(1)


def lowestCommonAncestor(root, p, q):
    current = root

    while current:
        if p.val > current.val and q.val > current.val:
            current = current.right
        elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
            return current

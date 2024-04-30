"""
Given a binary tree, determine if it is
height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false


Example 3:
Input: root = []
Output: true

Notes:

A balanced tree is a tree where the depth of each subtree
is not more than 1.

"""

# Time complexity: O(n)
# Space complexity: O(h) h = height


def isBalanced(root):
    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1] >= 1)

        return [balanced, 1 + max(left, right)]

    return dfs(root)[0]

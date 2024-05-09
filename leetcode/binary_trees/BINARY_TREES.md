# Binary Tree

Types of Binary Trees:

1. Full Binary Tree
2. Perfect Binary Tree
3. Complete Binary Tree
4. Balanced Binary Tree

### Full Binary Tree

This tree is a special type of binary tree in which
every parent node has either two children or no children

### Perfect Binary Tree

This tree will have nodes that have exactly two child nodes and all the leaf nodes are at the same level

### Complete Binary Tree

Similar to a full binary tree, but with some major differences:

1. Every level must be completely filled
2. All the leaf elements must lean towards the left
3. The last leaf element might not have a right sibling

### Balanced Binary Tree

A type of binary tree in which the difference between the height of the left and right subtree for each node is either 0 or 1.

## Common Pattern

The most common pattern I've noticed being used to solve binary tree problems is DFS.

With a recursion DFS, we don't have to worry about revisiting previous nodes as recursin uses a stack to keep track of function calls. As these calls return, they get popped off the call stack. This is what will enable the traversal to move back up the tree after exploring the left subtree and then continue to explore the right subtree.

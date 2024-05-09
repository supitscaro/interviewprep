"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Notes:
we can use a hash map to store which bracket belongs to which bracket:
brackets = {
 "}": "{",
 "]": "[",
 ")": "("
}

I know a stack could potentially be helpful here but trying to figure out why.
I could loop through the string and add each bracket into the stack but other than taking up space
it doesn't do much.

We could check if the current bracket we're in is in the brackets hash. and if it is, just remove it from the stack.
We could maybe check if the length of the stack is even but that doesn't actually take into account the matching pairs.
We could though check if the length of s is even before doing any of the other logic, cause if it's not we can just return false

But back to the loop. Maybe we check if the current bracket is in the hash. If it's not, then add it to the stack. If it is, then
we do a .pop()
"""


def isValid(s):
    if s % 2 != 0:
        return False

    stack = []
    bracket_hash = {"}": "{", "]": "[", ")": "("}

    for bracket in s:
        if bracket in bracket_hash:
            if stack and stack[-1] == bracket_hash[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    if len(stack) == 0:
        return True

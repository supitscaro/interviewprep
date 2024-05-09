"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

We could do a simple loop from the end of x and add each element to a new variable. we could then compare that variable to x and if it's
true, then return True. Else return False.
"""


def isPalindrome(x):
    new_x = ""
    string_x = str(x)

    for i in range(len(string_x) - 1, -1, -1):
        new_x += string_x[i]

    if string_x == new_x:
        return True

    return False

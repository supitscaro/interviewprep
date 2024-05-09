"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Note:
to keep track of how often a number appears, we could use a hash table
if we've seen that number already, increment the value. if we haven't, then add it
to the hash.

we can then loop through the dictionary and return the number that shows up once

these would mean two loops though which I believe is O(2n)
"""


def singleNumber(nums):
    seen = {}

    for _, value in enumerate(nums):
        if value in seen:
            seen[value] += 1
        else:
            seen[value] = 1

    for key, value in seen.items():
        if value == 1:
            return key

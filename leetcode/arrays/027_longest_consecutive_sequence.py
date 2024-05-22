"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


def longestConsecutive(nums):
    numsSet = set(nums)
    longest = 0

    for num in nums:
        # checks if there is a smaller number than the current one
        # and if there is then the current one is not the start
        # of the sequence
        if (num - 1) not in numsSet:
            length = 0

            # continue to check if the current number and current
            # num + 1 is in the numsSet. This indicates a
            # consecutive sequence so we should keep track of its
            while (num + length) in numsSet:
                length += 1

            longest = max(longest, length)

    return longest

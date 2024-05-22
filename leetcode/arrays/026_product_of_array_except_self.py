"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


def productExceptSelf(nums):
    left_multiplier = 1
    right_multiplier = 1

    left_arr, right_arr = [0] * len(nums), [0] * len(nums)

    for start in range(len(nums)):
        # so in [1,2,3,4], if nums[start] is 1, nums[end] will be 4
        end = -start - 1

        left_arr[start] = left_multiplier
        right_arr[end] = right_multiplier

        left_multiplier *= nums[start]
        right_multiplier *= nums[end]

    return [left*right for left, right in zip(left_arr, right_arr)]

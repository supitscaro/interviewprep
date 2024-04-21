# Given an array of integers nums which is sorted in
# ascending order, and an integer target, write a function
# to search target in nums. If target exists, then return its
# index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


"""
For example,

nums = [-1,0,3,5,9,12], target = 9

We can have two pointers for this problem. We will have one pointer at nums[0]
and another pointer at nums[-1] (or last element).

We can do a while loop where left <= right.

From the left pointer, we can find the mid point, which we can get by subtracting
right - left and dividing that by two. We can then add that to the left pointer to get the
mid point.

We can then check if the nums[midpoint] < target, and if it is we can move up the left pointer to
be midpoint + 1. We can also check if nums[midpoint] > target, we can then move the right pointer to
be midpoint - 1. And we can also then just return midpoint
"""


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        midpoint = left + ((right - left) // 2)

        if nums[midpoint] < target:
            left = midpoint + 1
        elif nums[midpoint] < target:
            right = midpoint - 1
        else:
            return midpoint

    return -1

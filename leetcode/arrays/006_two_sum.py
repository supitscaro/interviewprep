"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

nums = [3,2,4], target = 6

if our list length is just 2, can we assume that the two elements will add up to target?
if so, we should just return that

 if len(nums) == 2:
    return nums

so maybe we could compare the current element and every element after it?
 3 + 2 = 5
 3 + 4 = 7
 2 + 4 = 6
the thing here is...what happens if we get to the last element? but that wouldn't
really be an issue right? because if the combinations from 3 and 2 didn't work and
we HAD to add 4 to something else...there would be nothing to add it to

so i think this could be a good first approach, but prob not the best one.

One thing to note about the previous approach is that we don't care about what we've already seen. we're focusing
only on what is yet to come.
There is another way to solve this which would do the opposite aka we'd care about what's already been seen.

We can use a hash table for this. The goal would be to jot down or store the values we've encountered. This way
we can continue to move down the list and compare with what we've seen.

Let say we have [3, 2, 4] and a target == 6. We also have a seen = {}

We could loop through the list and if the current item we're on isn't in the seen hash, then we add it. We can
also check if the target - num is in the seen hash. This would mean that we've come across the number we could add
to the current number to get the target number
"""


# not ideal
def two_sum(nums, target):
    if len(nums) == 2:
        if nums[0] + nums[1] == target:
            return [0, 1]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def optimized_two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return seen


def two_pointer_two_sum(nums, target):
    sorted_nums = sorted((num, index) for index, num in enumerate(nums))

    left, right = 0, len(sorted_nums) - 1

    while left <= right:
        value = sorted_nums[left][0] + sorted_nums[right][0]
        if value == target:
            return [sorted_nums[left][1], sorted_nums[right][1]]
        elif value < target:
            left += 1
        else:
            right -= 1

    return []

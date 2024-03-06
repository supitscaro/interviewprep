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

so i think this could be a good first approach, but prob not the best one
"""

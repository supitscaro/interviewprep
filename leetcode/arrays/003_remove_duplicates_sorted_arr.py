"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Real world scenario:
we have a shelf with books; some are duplicated, some are not. we want to make sure only unique books are within the first few books. any repeated ones need to go to the back.

this won't be like previous examples where we compare the first and last items and then swap. since its in ascending order and there are duplicates, we might need to compare the first two.

however i think we might need to track the the last element anyway so we can place them there. we just need to make sure that what gets returned are all unique in their order.

what if we had a pointer to the start and pointer to the next item on the list. then we can compare nums[start] == nums[next]. if they are the same, get nums[last] and set it to nums[next]. decrement the last pointer and increment the next pointer.

then we compare nums[start] again to nums[next], which would be on the third element now. if nums[start] == nums[next], then swap it with nums[last] but if not, move both pointers.

the issue with this, also, is...what happens if items are repeated 3+ times?

the above idea doesn't fully work. adjusting the array like that will mess us up a bit

what we can do is have the two pointers, start and next. compare the two. if next is unique, then we need to swap nums[start] = nums[next] and increment the start pointer. this will do the swap to make sure the unique number is at the start of the array
"""

def removeDuplicates(nums):
  start = 0

  for checker in range(1, len(nums)):
    if nums[start] != nums[checker]:
      nums[start] = nums[checker]
      start += 1

  return start + 1

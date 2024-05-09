"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Real world scenario:
imagine we have two lines of people who were given a card with a number.
they've been put in ascending order. line A (nums1), has extra space for the people in line B (nums2). Try to merge these two in such a way that you don't need extra space

"""

def merge(nums1, m, nums2, n):
  mpointer, npointer, last = m - 1, n - 1, m + n -1

  while npointer >= 0:
    if mpointer >= 0 and nums1[mpointer] > nums2[npointer]:
      nums1[last] = nums1[mpointer]
      mpointer -= 1
    else:
      nums1[last] = nums2[npointer]
      npointer -= 1

    last -= 1

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# mpointer = 3 - 1 = 2
# npointer = 3 - 1 = 2
# last = 3 + 3 - 1 = 5 <- gets us the last index

# first loop:
#         (2)
# while npointer >= 0:
#                 (3)       (6)
#   if 2 >= 0 and nums1[2] > nums2[2]:
#     nums1[5] = nums1[2]
#     mpointer = 3 - 1 = 2
#   else:
#                 (6)
#     nums1[5] = nums2[2] <- we hit this
#     npointer = 3 - 1 = 2
# last = 4

# nums1 should now be [1,2,3,0,0,6]
# npointer is now 1
# mpointer is still 2
# last is now 4

# second loop:
#       (1)
# while npointer >= 0:
#               (3)           (5)
#   if 2 >= 0 and nums1[2] > nums2[1]:
#     nums1[4] = nums1[2] (which is 3)
#     mpointer -= 1
#   else:
#                 (5)
#     nums1[4] = nums2[1] <- we hit this
#     npointer = 1 - 1 = 0
# last = 3

# nums1 should now be [1,2,3,0,5,6]
# npointer is now 0
# mpointer is still 2
# last is now 3

# third loop
#         (0)
# while npointer >= 0:
#                 (3)       (2)
# if 2 >= 9 and nums1[2] > nums2[0]:
#   nums1[3] = nums1[2] (which is 3) <- we hit this
#   mpointer -= 1 (2 - 1) = 1
# else:
#   nums1[3] = nums2[0]
#   npointer -=1
# last = 2

# nums1 should now be [1,2,3,3,5,6]
# npointer is still 0
# mpointer is now 1
# last is now 2

# fourth loop
#         (0)
# while npointer >= 0:
#               (2)         (2)
# if 1 >= 0 and nums1[1] > nums2[0]:
#   nums1[2] = nums1[1]
# else:
#   nums1[2] = nums2[0] (which is 2) <- we hit this
#   npointer -= 1 (so it's now -1)
# last = 1

# nums1 is now [1,2,2,3,5,6]
# npointer is now -1
# mpointer is still 1
# last is now 1
# we no longer go into the while loop

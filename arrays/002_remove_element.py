"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Real world scenario:
Imagine a shelf in a bookcase. We want to arrange it by a given color. We want to do this without having to place the books anywhere else though and the books that don't match the color need to be moved to the right of the shelf.

so assume we have this shelf
[red, blue, blue, red] similar to [3,2,2,3].

Let's say we want to move the books that aren't red to the start of the shelf, so all blue books go to the start aka the left side.

we could look at the start and the end of the shelf. Compare the books' color and swap them only if the book on the left isn't blue.

if the color isn't blue, then we go to the second book on the left and compare that color to the last book.

we can continue this pattern until we get all of the blue books to the start or left side of the shelf
"""

def removeElement(nums, val):
  start = 0
  end = len(nums) - 1

  while start <= end:
    if nums[start] != val:
      start += 1
    else:
      nums[start] = nums[end]
      end -= 1

  return start

# nums = [3,2,2,3], val = 3
# start = 0
# end = 3

# First Loop
# while 0 <= 3:
#       (3)
#   if nums[0] != 3:
#     start += 1
#   else:
#     nums[0] = nums[3] <- we hit this
#     end -= 1

# After first loop
# nums[3,2,2,3]
# start = 0
# end = 2

# Second Loop
# while 0 <= 2:
#       (3)
#   if nums[0] != 3:
#     start += 1
#   else:
#       (3)      (2)
#     nums[0] = nums[2]
#     end -= 1

# After second loop
# nums[2,2,3,3]
# start = 0
# end = 1

# Third Loop
# while 1 <= 1:
#       (2)
#   if nums[1] != 3:
#     start += 1
#   else:
#     nums[1] = nums[1]
#     end -=1

# I'm not too positive on that last loop BUT hoping its right

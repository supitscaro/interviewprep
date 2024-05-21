"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Bucket Sort:
- an algorithm to sort items and put them in a category
- we can create a dict to keep count of how often a number appears
- we can then have a frequency variable that will originally be a list
  of empty lists.
- we can loop through the dict and then place the numbers in the
  frequency variable based on how often they came up in the nums list
  - for example, if we have [1,1,1,2,2,3] we can place the number `1`
    in the 3rd index because it shows up 3 times
- from there, we can loop through the frequency list. we should do this
  from the end of the list to the beginning. The items that show up the most
  will be towards the end of the frequency list. So we can loop through the list
  and break out if we've gone past the "k" amount
- then just return the result
"""


def topKFrequent(self, nums, k):
    count_map = {}
    frequency = [[] for i in range(len(nums) + 1)]

    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num, count in count_map.items():
        frequency[count].append(num)

    result = []

    for i in range(len(frequency) - 1, 0, -1):
        if frequency[i]:
            result.extend(frequency[i])

        if len(result) >= k:
            break

    return result

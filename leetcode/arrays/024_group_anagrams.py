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
"""


def groupAnagrams(strs):
    hash_map = {}

    for word in strs:
        sorted_word_list = sorted(word)
        sorted_word = ''.join(sorted_word_list)

        if sorted_word in hash_map:
            hash_map[sorted_word].append(word)
        else:
            hash_map[sorted_word] = [word]

        return list(hash_map.values())

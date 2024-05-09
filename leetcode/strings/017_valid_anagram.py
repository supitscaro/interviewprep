"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    map = {}

    for char1 in s:
        if char1 in map:
            map[char1] += 1
        else:
            map[char1] = 1

    for char2 in t:
        if char2 in map:
            map[char2] -= 1
        else:
            map[char2] = 1

    for item in map:
        if map[item] > 0:
            return False

    return True

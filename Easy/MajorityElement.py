"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from collections import defaultdict
# The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash_table = defaultdict(int)

        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
            if hash_table[i] > len(nums)//2:
                return i
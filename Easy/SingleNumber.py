"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hash_table = defaultdict(int)

        # make hash with key as num in nums and value as number of times appeared in nums
        # ex. [4,1,2,1,2] will make hash as {4:1, 1:2, 2:2}
        for i in nums:
            hash_table[i] += 1

        # during the loop, if given i in hash has only 1 as its value, then return that i
        for i in hash_table:
            if hash_table[i] == 1:
                return i
        
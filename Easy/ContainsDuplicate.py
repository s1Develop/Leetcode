"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        save = {}

        for i in nums:

            # check if i is one of key in save
            if i in save:
                return True
            
            # save[i] refers to value associated with the key i 그니까 i가 key이고 save[i]라고 하면 value
            # 그래서 save[i] = j 이라고 하면 i라는 key에 j를 value로 넣는다는 말
            save[i] = i
        return False
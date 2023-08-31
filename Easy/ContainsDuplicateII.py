"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


# k is the max allowed difference between the indices i and j such that nums[i]==nums[j]
# and abs(i-j) <= k.
# 그니까 nums[i]이랑 nums[j] 값이 똑같고 그 i랑 j의 거리자체가 최대 k만큼 벌어져있다는 말.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        check = {}

        for i in range(len(nums)):

            # check if i is one of key in check
            # if i in check:

            # check if nums[i] is one of value in check
            # if nums[i] in check.values():

             # check if nums[i] is one of key in check
            if nums[i] in check:

                # check if abs(i-j) <= k
                if (i - check[nums[i]]) <= k:
                    return True
            
            # store i as a value of nums[i] in check
            check[nums[i]] = i
        return False
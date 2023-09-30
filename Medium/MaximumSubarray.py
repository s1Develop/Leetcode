"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP

        # set both current_subarray and max_subarray to be the first element of nums
        current_subarray = max_subarray = nums[0]

        # num goes through starting from second element of nums to last
        for num in nums[1:]:

            # current_subarray는 num을 돌릴때마다 num이랑 current_subarray+num을 비교해서 큰애로 업데이트해준다
            current_subarray = max(num, current_subarray + num)

            # max_subarray는 각 loop당 max_subarray랑 current_subarray를 비교해서 큰애로 계속 업데이트 해준다
            max_subarray = max(max_subarray, current_subarray)

        # 마지막에 max_subarray를 가져온다
        return max_subarray

        
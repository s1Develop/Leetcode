"""
1493. Longest Subarray of 1's After Deleting One Element
Solved
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):

            # count the # of zero count
            if nums[right] == 0:
                zero_count += 1

            # find the current length of subarray
            # 만약 제로 카운트가 1이상이면 left를 옆으로 옮기고
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                
                # 제로 카운트가 1이상이면 무조건 left는 일단 slide
                left += 1

            # cur length of subarray랑 max_length비교해서 업데이트
            max_length = max(max_length, right-left)
        return max_length


        
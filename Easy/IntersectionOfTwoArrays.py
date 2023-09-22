"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        con = {}
        for i in nums1:
            con[i] = 0
        
        for j in nums2:
            if j in con:
                con[j] = 1

        # The items() method returns a view object. 
        # The view object contains the key-value pairs of the dictionary, as tuples in a list.
        # k, v in con.items()는 대충 k가 key, v가 value로 key-value tuple pairs인 con.items안에서 찾는 것
        #그래서 결국 value값이 1인애들만 []안에 k를 넣어준다.
        return [k for k, v in con.items() if v == 1]
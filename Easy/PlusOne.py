"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        # n is a length of the list
        n = len(digits)

        for i in range(n):
            # checking each index from the last
            index = n - 1 - i

            # if the current index is 9
            if digits[index] == 9:
                # then the number in the index is set to be 0
                digits[index] = 0

            # if the current index is not 9
            else:

                # then increment the current number by 1
                digits[index] += 1

                # and then return the list
                return digits

        # this is the case when all of the digit in the list are 9
        return [1] + digits
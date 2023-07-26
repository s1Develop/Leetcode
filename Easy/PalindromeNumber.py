"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if negative, false anyway
        if x<0:
            return False
        
        #copy the given integer to temp
        temp = x

        #initialize reverse_num
        reverse_num = 0

        while temp != 0:

            # last digit of temp
            last_digit = temp % 10 

            # reverse current number
            reverse_num = (reverse_num * 10) + last_digit

            # remove last digit from the number
            temp = temp // 10        

        # check if what we reverse is same as the original number
        return x == reverse_num
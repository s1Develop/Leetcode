"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1

        while i < j:

            # i값이 j값보다 작고 i가 alphabet이 아니라면
            while i < j and not s[i].isalnum():
                # i값 늘려주기
                i += 1

            # i값이 j값보다 작고 j가 alphabet이 아니라면
            while i < j and not s[j].isalnum():
                # j값 줄여주기
                j -= 1

            # .lower() 자체가 바로 lower로 만들어주기 때문에 바로 비교 가능
            if s[i].lower() != s[j].lower():
                return False
            

            i += 1
            j -= 1

        return True




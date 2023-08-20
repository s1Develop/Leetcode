"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
"""
"""
given a string of length 1, the ord() function returns an integer representing the Unicode code point of the character when an argument is a Unicode object, or the value of the byte when the argument is an 8-bit string
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        temp = 0
        n = len(s)
        for i in range(n):
            temp = temp*26
            temp += (ord(s[i]) - ord('A') + 1)
        return temp
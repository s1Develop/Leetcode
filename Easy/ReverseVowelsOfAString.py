"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # choose which DS to use
        # tuple: immutable, set: mutable and no duplicate elements, dictionary: mutable and no duplicates key
        vowels = 'aeiouAEIOU'

        vowels_stack = []

        sorted = ''

        for char in s:
            if char in vowels:
                vowels_stack.append(char)
        for char in s:
            if char in vowels:
                sorted += vowels_stack.pop()
            else:
                sorted += char
        return sorted
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

        temp = ''

        # 먼저 s안에 있는 모든 vowels들을 vowels_stack안에 다 넣는다
        for char in s:
            if char in vowels:
                vowels_stack.append(char)

        # 다시 loop를 돌려서 s안에서 vowel이라면 stack안에서 pop되는 애(즉 s안에서 마지막에 있던 애를)를 temp안에 넣어준다
        # 만약 vowel이 아니라면 그냥 그대로 각각 temp안에 각각의 current index in s를 넣어준다.
        for char in s:
            if char in vowels:
                temp += vowels_stack.pop()
            else:
                temp += char
        return temp
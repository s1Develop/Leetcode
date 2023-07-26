"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # 마지막 word의 마지막 index를 찾아서 p에 넣기
        p = len(s) -1
        while p >= 0 and s[p] == " ":
            p -= 1
        
        # 여기선 p의 index가 마지막 word의 마지막 index인게 확실하니
        # 그 index부터 decrease되면서 마지막 word의 첫번째 index까지 도달하게 하고
        # 그렇게 내려갈때마다 length에다가 1을 추가하면서 마지막 word의 length를 구하기
        length = 0
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1
        return length
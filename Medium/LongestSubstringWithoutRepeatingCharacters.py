"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this method is called sliding window. 
        # moves from left to right and contains only unique characters
        n = len(s)

        # keeps track of the maximum length of the window seen so far.
        ans = 0

        mp = {}

        # represents the start of the current window.
        i = 0

        # s[j]라는건 대충 given str에서 each alphabet을 뜻하는거
        # mp[s[j]]라는건 대충 mp라는 hash에서 s[j]의 value를 뜻한
        # j represent the end of the current window.
        for j in range(n):

            # 만약 s안에 current j값이 mp에 들어가 있으면, i즉 start of the current window를 
            # 그 mp안에 있는 s[j]의 값과 i를 비교해서 큰애를 i로 잡는다
            if s[j] in mp:
                i = max(mp[s[j]], i)

            # ans즉 max length of the window so far을 자기자신이랑 length of the current window
            # 랑을 비교해서 max값으로 다시 세팅한다.
            ans = max(ans, j-i+1)

            # last occurence of the character is now j and next occurence of the character's index is j+1
            mp[s[j]] = j+1

        return ans
"""

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # Creating a Counter object: 
        # The Counter function takes a string s as input and returns a Counter object, 
        # which is a dictionary where keys are the characters in s
        # and values are the counts of each character.
        # 대충 각 alphabet을 key로 잡고 그 애들의 count를 value로 잡는 dictionary를 만든다
        count = collections.Counter(s)
        
        # The enumerate function is used to get both the index (idx)
        # and character (c) of the string s.
        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1
"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # 이게 가능한 이유는 대충 t를 s+s로 잡고 했을때 t[1:-1]안에 s가 있는지 체크하는 이유는
        # 즉 'abcabc'를 보면 t[1:-1]은 'bcabcabcab'가 되는데 여기서 bc'abcabc'ab 이렇게만
        # 확인하면 되기에
        t = s + s
        if s in t[1:-1]:
            return True
        return False

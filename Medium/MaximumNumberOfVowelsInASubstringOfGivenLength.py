"""
1456. Maximum Number of Vowels in a Substring of Given Length
Solved
Medium
Topics
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel = {'a','e','i','o','u'}

        count = 0
        m_vowels = 0

        # 처음부터 k까지 vowel카운트를 최대한 시킨다
        for i in range(k):
            if s[i] in vowel:
                count = count + 1
                m_vowels = max(count, m_vowels)
        
        i=0
        # k부터 마지막까지 loop
        for j in range(k, len(s)):
            # 만약에 j에 vowel이 있으면 카운트 하나 더 추카
            if s[j] in vowel:
                count = count + 1
            # max가 k여야하기에 decrement
            if s[i] in vowel and k>1:
                count = count - 1
            i += 1
            m_vowels = max(m_vowels, count)
        return min(m_vowels, k)


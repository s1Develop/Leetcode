"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # use string.split(" ") function

        # words is a list of str containing each word from s splitted by " "
        words = s.split(" ")

        # split해놓은 list of word의 길이가 pattern의 길이랑 다르면 return False
        if len(words) != len(pattern):
            return False

        # hash_char은 대충 pattern안에 있는 애들을 key로 잡은 해쉬
        hash_char = {}

        # hash_word는 대충 s안에 있는 애들을 key로 잡은 해쉬
        hash_word = {}

        for i in range(len(pattern)):
            c = pattern[i]
            w = words[i]

            if c not in hash_char:

                # 만약 c가 hash_char에 없는데 현재 위치의 w가 hash_word안에 있으면 return False
                if w in hash_word:
                    return False

                # 만약 c가 hash_char에 없는데 현재 위치의 w가 hash_word안에 없으면 업데이트
                else:
                    hash_char[c] = w
                    hash_word[w] = c

            #만약 c가 hash_char에 있으면
            else:
                if hash_char[c] != w:
                    return False
        return True
                    
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        # 1. 일단 haystack안에 needle이 들어가 있냐 안있냐를 체크

        # 2. 들어있다면 그 needle의 첫번째 index를 가져오기

        m = len(needle)
        n = len(haystack)

        # haystack의 길이 빼기 needle길이 더하기 1한거 즉 0부터 haystack - needle한거
        for i in range(n-m+1):

            # 0부터 len(needle)한거
            for j in range(m):

                # inner loop index이 있는 needle에 있는 애가 haystack[i+j]값이랑 다르면
                if needle[j] != haystack[i+j]:
                    #브레이크 즉 이 for loop안에서 아예 빠져나가기
                    break

                # 만약 j가 needle의 len - 1한거랑 같으면
                if j == m-1:
                    # outer loop의 index를 return하기
                    return i
        return -1
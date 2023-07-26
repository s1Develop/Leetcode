"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        v = sorted(strs) #sorted함으로써 처음이랑 마지막꺼만 비교를하면 되는게 된다.

        #결국 lexicographically order로 했으니까 처음이랑 마지막애만 가지고 비교
        firstWord = v[0]
        lastWord = v[-1]

        # for loop자체를 first랑 last중의 len가 낮은 애만큼 돌리면서
        for i in range(min(len(firstWord), len(lastWord))):
            #만약에 current index의 alphabet이 다르다 싶으면 지금 현재의 common를 return시키면 된다
            if firstWord[i] != lastWord[i]:
                return common
            #아니라면 current index의 alphabet을 common에 넣는다
            common = common + firstWord[i]
        
        # for loop이 다 돌았다는 말 이기때문에 common을 그대로 return한다.
        return common
            
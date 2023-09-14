"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        # 먼저 hashmap으로 key value 값을 정한다 (T0, T1, T2인 상황)
        dp = {0:0, 1:1, 2:1}

        def dfs(i:int) -> int:

            if i in dp:
                return dp[i]

            #hash map에다가 3~n까지의 숫자들을 넣어준다
            dp[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return dp[i]

        return dfs(n)
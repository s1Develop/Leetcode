"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

#결국 어렵게 생각할 필요가 없다.
#그냥 recursion을 써서 돌리면 끝
#하지만 recursion을 써버리면 time complexity가 2^n이 되기에
# 320에서 배운 memoization 즉 recursion중에서 redundant한 calculation들을 없애주는 것.

class Solution:
    def climbStairs(self, n: int) -> int:
        #memo is an unordered mapto store the already computed results for each step n.
        memo = {}
        return self.helper(n, memo)
    


    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
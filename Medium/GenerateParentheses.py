"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 맨 처음에 항상 0,0,''으로 시작
        def dfs(left, right, s):

            # 만약 parameter s의 길이가 n에 2곱한거랑 같다면
            if len(s) == n*2:
                res.append(s)
                return

            # parameter left가 n값보다 작다면
            if left < n:
                # dfs를 left에 1을 추가한거에다가 '('를 넣어서 다시 부르기
                dfs(left + 1, right, s + '(')

            # parameter right이 left값보다 작다면
            if right < left:
                # dfs를 right에 1을 추가한거에다가 ')'를 넣어서 다시 부르기
                dfs(left, right + 1, s + ')')

        # if len(s) == n*2를 들어감으로서 마지막에 있는 괄호를 닫게 된다
        # if left < n이랑 if right < left를 같이 들어가면서 괄호를 열었다가 닫을 수 있다

        res = []
        dfs(0,0,'')
        return res


    # 	    	    	   	(0, 0, '')
    # 	    	    	   	    |	
    # 	       	    		(1, 0, '(')  
    # 	      	    	   /           \
    #       		(2, 0, '((')      (1, 1, '()')
    #       		   /                 \
    #       	(2, 1, '(()')           (2, 1, '()(')
    #       	   /                       \
    #       (2, 2, '(())')                (2, 2, '()()')
    #   	      |	                         |
    #    res.append('(())')            res.append('()()')

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:

                #만약에 current char이 close bracket인데 stack이 empty일때 False 리턴하기
                if not stack:
                    return False

                #만약 current char이 )이고 stack맨뒤에 애가 (이면 stack에 맨뒤애 빼기
                if char == ')' and stack[-1] == '(':
                    stack.pop()

                #만약 current char이 ]이고 stack맨뒤에 애가 [이면 stack에 맨뒤애 빼기
                elif char == ']' and stack[-1] == '[':
                    stack.pop()

                #만약 current char이 }이고 stack맨뒤에 애가 {이면 stack에 맨뒤애 빼기
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        #맨 마지막에 stack이 empty이면 True를 리턴한다는 것
        return not stack
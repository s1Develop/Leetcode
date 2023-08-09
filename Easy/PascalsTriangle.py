"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for rowNum in range(numRows):

            # list comprehension 대충 row라는 list에다가 모든 index에 None을 넣어준다는 말
            row = [None for _ in range(rowNum + 1)]

            # 그리고 처음이랑 마지막 element들만 1로 넣어주는 것.
            row[0], row[-1] = 1, 1

            # 이 loop은 대충 range(1, 0)이나 range(1,1)일때는 loop자체가 안돌아간다
            for j in range(1, len(row) - 1):

                row[j] = triangle[rowNum - 1][j - 1] + triangle[rowNum - 1][j]

            triangle.append(row)
            
        return triangle

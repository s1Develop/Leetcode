"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # list의 첫 element를 1로 잡고 각 inner loop에서 계속 row를 overlap시킨다.
        row = [1]

        # given rowIndex까지 outer loop을 돌린다
        for i in range(rowIndex):

            # i부터 0 직전 즉 1까지 -1씩 내려가는것
            for j in range(i,0,-1):

                # 그전 outloop에서 만들어졌던 row를 가지고 더한다
                row[j] = row[j] + row[j-1]

            # 각 list의 마지막에 1를 추가하고 inner loop을 끝낸다
            row.append(1)
        return rowclass Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # list의 첫 element를 1로 잡고 각 inner loop에서 계속 row를 overlap시킨다.
        row = [1]

        # given rowIndex까지 outer loop을 돌린다
        for i in range(rowIndex):

            # i부터 0 직전 즉 1까지 -1씩 내려가는것
            for j in range(i,0,-1):

                # 그전 outloop에서 만들어졌던 row를 가지고 더한다
                row[j] = row[j] + row[j-1]

            # 각 list의 마지막에 1를 추가하고 inner loop을 끝낸다
            row.append(1)
        return row
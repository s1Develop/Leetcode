"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # current row index
        idx = 0

        # if d = 1, we go downwards, if d = -1, we go upward
        d = 1

        # create a list of empty list for numRows times
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)

            # if we are at top row, we change d to 1 and go downwards
            if idx == 0:
                d = 1

            # if we are at bottom row, we change d to -1 and go upwards
            elif idx == numRows - 1:
                d = -1
            
            # do this every loop
            idx += d
        
        # concatenate all the strings in each row
        # ex. row0= PIN, row1=ALSIG, row2=YAHR, row3=PI    for "PAYPALISHIRING"
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        # concatenate all the row in rows (if '#'.join(rows), then concatenate all string but add # in between)
        return ''.join(rows)
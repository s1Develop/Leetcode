"""
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Use Two Pointer one from left and one from right. Update Max area by comparing with current area.
        Repeat this until left and right become equal.
        """
        left = 0
        right = len(height)-1

        maxArea = 0

        while left < right:
            minHeight = min(height[left], height[right])
            currentArea = minHeight * (right-left)

            maxArea = max(maxArea, currentArea)

            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1

        return maxArea
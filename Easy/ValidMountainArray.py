"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        right = len(arr)
        left = 0

        # left값이 right 인덱스 가기 직전까지와 arr[left]값이 그 다음오는 값보다 낮을때까지
        # 대충 왼쪽에서부터 마운틴 피크까지 간다는거
        while left+1 < right and arr[left]<arr[left+1]:
            left = left + 1

        # 만약 left값이 위에 while룹에서 변화가 없거나, 마지막 인덱스까지 가버렸다면
        if left == 0 or left == right-1:
            return False

        # 대충 피크에서부터 오른쪽 끝까지 계속 간다는 것
        while left + 1 < right and arr[left] > arr[left+1]:
            left += 1
        
        # 현재 left값이 right값과 같으면 return True
        return left == right-1
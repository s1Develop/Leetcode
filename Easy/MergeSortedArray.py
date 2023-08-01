"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #이 문제 자체가 nums1의 len가 num1의 # of elements들이랑 num2의 # of elements들이랑 더한값이
        #같다는 조건이다. 그래서 밑에 for loop이 가능

        # p1은 대충 nums1의 길이가 아닌 마지막 element의 index를 나타낸다.
        p1 = m-1

        # p2는 대충 nums2의 마지막 element의 index를 나타낸다.
        p2 = n-1

        # the range will start at n + m - 1
        #  and decrement by 1 until it reaches -1 (not inclusive)
        # n+m-1부터 시작해서, -1까지 내려가고 각 loop마다 1씩 내려간다는 말
        # 그니까 (start-value, stop-value, step-value)
        for p in range(n + m - 1, -1, -1):

            #결국 nums1을 바꾸라는건데 p2가 즉 nums2의 # of elements가 없으면 그대로 nums1를 놔두면 끝
            if p2 < 0:
                break

            # 현재 p1값이 0보다 크거나 같고, 
            # nums1안에 p1의 index에 있는 값이 nums2안에 현재 p2의 index에 있는 값보다 크다면
            if p1 >= 0 and nums1[p1] > nums2[p2]:

                # loop의 index인 p index의 nums1의 element값을 p1 index에 있는 값으로 바꾼다
                nums1[p] = nums1[p1]

                #그러고 p1값을 1 decrement해준다
                p1 -= 1
            
            # 현재 p1값이 0보다 작거나
            # nums1안에 p2의 index에 있는 값이 nums2안에 현재 p2의 index에 있는 값보다 작거나 같으면
            else:
                
                # loop의 index인 p index의 nums1의 element값을 nums2에 있는 p2 index의 element 값으로 바꾼다
                nums1[p] = nums2[p2]

                #그러고 p2값을 1 decrement해준다
                p2 -= 1


"""
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

first loop
1. p = 0 that is the last index of nums1, p1 = 3 that is the last element of nums1, p2 = 6 that is the last element of nums2
2. since nums1[1] <= nums2[p2], 즉 else case로 가게 돼서 nums1의 맨 마지막 element값을 nums[p2] 값으로 바꿔준다. 
    왜냐면 이 조건이 nums[p2]가 크다는걸 알게 했으니

second loop
1. p = 0 that is second last index of nums1, p1 = 3 that is the last element of nums, p2 = 5 that is the second element of nums2
2. since nums1[p1] <= nums[p2], 즉 else case로 가게 돼서 nums1의 뒤에서 두번째 element값을 nums[p2] 값으로 바꿔준다.

third loop
1. p = 0 that is third last index of nums1, p1 = 3 that is the last element of nums, p2 = 2 that is the first element of nums2
2. since nums1[p1] > nums[p2], 즉 if p1 >= 0 and nums1[p1] > nums2[p2]: 로 가기때문에 nums[p]에 있는 값을 nums[p1]값으로 바꿔주게 된다.

...

"""
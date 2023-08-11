"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 일단 temp를 prices의 첫 element로 잡고
        temp = prices[0]

        # value값을 0으로 잡는다
        val = 0

        # loop를 0부터 prices의 마지막 index까지 돌린다
        for i in range(len(prices)):

            # 현재 temp값이 현재 prices의 i index의 값보다 크다고 하면
            if temp > prices[i]:

                # temp값을 현재 prices의 i index의 값으로 바꾼다
                temp = prices[i]

            # 만약 temp값이 prices의 i index의 값보다 작거나 같으면
            elif temp <= prices[i]:

                # 거기서 prices의 i index의 값이랑 temp값을 비교했을때 현재 val값보다 클 경우
                if (prices[i] - temp) > val:

                    # val값을 price[i] - temp값으로 업데이트해준다
                    val = prices[i]-temp

        return valclass Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 일단 temp를 prices의 첫 element로 잡고
        temp = prices[0]

        # value값을 0으로 잡는다
        val = 0

        # loop를 0부터 prices의 마지막 index까지 돌린다
        for i in range(len(prices)):

            # 현재 temp값이 현재 prices의 i index의 값보다 크다고 하면
            if temp > prices[i]:

                # temp값을 현재 prices의 i index의 값으로 바꾼다
                temp = prices[i]

            # 만약 temp값이 prices의 i index의 값보다 작거나 같으면
            elif temp <= prices[i]:

                # 거기서 prices의 i index의 값이랑 temp값을 비교했을때 현재 val값보다 클 경우
                if (prices[i] - temp) > val:

                    # val값을 price[i] - temp값으로 업데이트해준다
                    val = prices[i]-temp

        return val
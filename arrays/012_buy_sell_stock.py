"""
You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Notes:

with that first example, the most profit would be if you buy when
it's at $1 and sell when it's at #7. But because $7 comes before the
$1, we can't really do this.

I can't buy something on the 12th day of the month and sell it on
the 11th day of that same month. So this means, as we solve this
problem...we can't ever look back to previous elements.

my original thought is to have two pointers, where one stores the first
number in the list and the other pointer is used to loop through the
array. The issue with this thought is that it's one loop just to
figure out one part of the problem and it's not even a full solution
"""


def maxProfit(prices):
    buy, sell = 0, 1

    max_profit = 0

    while sell < len(prices):
        # we have some profit
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
        else:
            buy = sell

        sell += 1

    return max_profit

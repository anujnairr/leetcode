# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

prices = [7, 1, 5, 3, 6, 4]

i = 0
j = i+1
result = 0
while j <= len(prices)-1:
    if prices[j] > prices[i]:
        result = max(result, prices[j] - prices[i])
    else:
        i = j
    j += 1
print(result)

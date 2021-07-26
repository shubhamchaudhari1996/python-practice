from collections import deque
def buy_sell(prices):
    max = 0
    prices = deque(prices)
    buy_price = prices.popleft()
    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            profit = price - buy_price
            if profit > max:
                max = profit

    if max:
        return max
    else:
        return -1

prices = list(map(int,input().split()))
# prices = [1, 2, 4, 5, 4, 2]
# prices.sort()
max_profit = buy_sell(prices)
print(max_profit)


# print(max_profit)

# def max_occ(lst,x):
#     count=0
#     for i in lst:
#         if (i==x):
#             count=count+1
#     return count

# lst=[1, 2, 4, 5, 4, 2]
# x=max(lst,key=lst.count)
# print(x,"occurs ",max_occ(lst,x),"times")

# from collections import defaultdict

# L = [1, 2, 4, 5, 4, 2]
# d = defaultdict(int)
# for i in L:
#     d[i] += 1
# result = max(d.items(), key=lambda x: x[1])
# print (result)

# Python program to find the
# frequency of largest element

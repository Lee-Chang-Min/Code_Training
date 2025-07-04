import sys

n = int(input()) # 카드 갯수 
prices = [0] + list(map(int, input().split()))


print(prices)
#[0, 1, 5, 6, 7]

# dp[k] : 카드 구매 금액의 최댓값
dp = [0] * (n + 1) 
#각 개수 별 카드 최대값

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + prices[k])

print(dp[n])


# i = 1:
#   k = 1: dp[1] = max(dp[1], dp[0] + prices[0]) = max(0, 0 + 1) = 1
# i = 2:
#   k = 1: `dp[2] = max(dp[2], dp[1] + prices[1]) = max(0, 1 + 1) = 2
#   k = 2: `dp[2] = max(dp[2], dp[0] + prices[2]) = max(2, 0 + 5) = 5
# i = 3:
#   k = 1: `dp[3] = max(dp[3], dp[2] + prices[0]) = max(0, 5 + 1) = 6
#   k = 2: `dp[3] = max(dp[3], dp[1] + prices[1]) = max(6, 1 + 5) = 6
#   k = 3: `dp[3] = max(dp[3], dp[0] + prices[2]) = max(6, 0 + 6) = 6
# i = 4:
#    k = 1: `dp[4] = max(dp[4], dp[3] + prices[0]) = max(0, 6 + 1) = 7
#    k = 2: `dp[4] = max(dp[4], dp[2] + prices[1]) = max(7, 5 + 5) = 10
#    k = 3: `dp[4] = max(dp[4], dp[1] + prices[2]) = max(10, 1 + 6) = 10
#    k = 4: `dp[4] = max(dp[4], dp[0] + prices[3]) = max(10, 0 + 7) = 10
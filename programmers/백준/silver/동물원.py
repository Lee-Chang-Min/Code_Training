import sys

N = int(input()) # 4개

dp = [[0] * 3 for _ in range(N)]


dp[0] = [1] * 3

for i in range(1, N):
    dp[i][0] = sum(dp[i-1]) % 9901

    dp[i][1] = dp[i-1][0] + dp[i-1][2] % 9901
    
    dp[i][2] = dp[i-1][0] + dp[i-1][1] % 9901

print(sum(dp[N-1]))



    
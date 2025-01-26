N = int(input())
wine = [0]

for _ in range(N):
    wine.append(int(input()))

dp = [0] * (N + 1) # 메모지로 활용

dp[1] = wine[1]

if N > 1:
    dp[2] = wine[1] + wine[2]


# dp[3] = max(dp[1] + wine[3],dp[2], dp[0]+wine[2]+wine[3])

#현재 포도주를 안마시는 경우 x,oox
#현재 포도주를 마시는 경우 ooxo
#현재 포도주를 마시는 경우2 oxoo



for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])


# print(wine)
print(dp[N])


# 6 + 10 + 13 
    # 6 + 10 + 9 
    # 6 + 13 + 9
import sys
input = sys.stdin.readline

# N 지름길 개수
# D 고속도로 길이 
N, D = map(int, input().split())


dp = [10001] * (D + 1)
dp[0] = 0

shortcuts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D: # 지름길이 도착위치보다 넘은거는 제외 해야함
        shortcuts.append((start, end, length))

#도로 시작 위치에서 정렬해야 할듯?
#인덱스 잡아서 sort
shortcuts.sort(key=lambda x: x[1]) # [(0, 50, 10), (0, 50, 20), (50, 100, 10), (110, 140, 90)]

for i in range(1, D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1) # 그냥 도로 dp[50] = dp[49] + 1 = 50.

    for start, end, length in shortcuts:
        if end == i and dp[start] + length < dp[end]:   
            dp[end] = dp[start] + length

print(dp[D])
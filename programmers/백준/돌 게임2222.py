

# 돌이 N-1 개 일때 진다
# 돌이 N-3 개 일때 진다

 
N = int(input())
dp = [0] * (1000 + 1)
 
# 초기값 설정
dp[1] = 1  # SK 승리
dp[2] = 2  # CY 승리
dp[3] = 1  # SK 승리

# 점화식 계산
for n in range(4, N + 1):
    dp[n] = min(dp[n - 1], dp[n - 3]) + 1

# 결과 판별 및 출력
if dp[N] % 2 == 1:  # 홀수 턴 -> SK 차례
    print("SK")
else:               # 짝수 턴 -> CY 차례
    print("CY")
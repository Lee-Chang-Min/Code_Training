def solution(n):
    if n == 1:
        return 1
    # n이 2일 경우도 미리 처리해주는 것이 좋습니다.
    if n == 2:
        return 2

    dp = [0] * (n + 1)

    # 기본값(base cases) 설정
    dp[1] = 1
    dp[2] = 2

    # 점화식을 이용하여 dp 테이블 채우기
    # 3부터 n까지 반복합니다.
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]


print(solution(4))
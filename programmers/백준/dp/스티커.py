T = int(input())

for _ in range(T):
    n = int(input())
    dp = [] 
    for _ in range(2):
        # 한 줄 입력을 받아 처리한 리스트를 바로 dp에 추가
        line_list = list(map(int, input().split()))
        dp.append(line_list)


    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])


    print(max(dp[0][n-1], dp[1][n-1]))
        
        


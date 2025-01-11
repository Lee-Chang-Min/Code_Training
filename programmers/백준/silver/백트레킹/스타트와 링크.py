
import sys

input = sys.stdin.readline
N = int(input()) # 전체 인원

status = [list(map(int, input().split())) for _ in range(N)] # 능력치

visited = [False] * N
result = sys.maxsize # 결과 큰 수로 초기화

def dfs(a, idx):
    global result

    if a == N // 2: # 반반으로 나뉘었을 경우

        # 각 팀의 능력치 초기화
        team_start = 0
        team_link = 0

        for i in range(N):
            for j in range(N):

                # 방문한 반을 start 팀으로 배정
                if visited[i] and visited[j]: 
                    team_start += status[i][j]

                # 방문하지 않은 반을 link 팀으로 배정
                elif not visited[i] and not visited[j]: 
                    team_link += status[i][j]

        result = min(result, abs(team_start - team_link))
        return

    else: # 인원 나누기
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(a + 1, i + 1)
                visited[i] = False

dfs(0, 0)
print(result)







# def cal(alst, blst):
#     asum = 0
#     bsum = 0
#     for i in range(M):
#         for j in range(M):
#             asum += arr[alst[i]][alst[j]]
#             bsum += arr[blst[i]][blst[j]]
#     return abs(asum-bsum)


# def dfs(n, alst, blst):
#     global ans
#     if n == N:
#         if len(alst) == len(blst):
#             ans = min(ans, cal(alst, blst))
#         return
    
#     dfs(n+1, alst+[n], blst)
#     dfs(n+1, alst, blst+[n])
    
#     # A팀 선택




# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]


# M = N//2

# ans = 100*M*M #큰수를 넣기 위해

# dfs(0,[],[])

# print(ans)

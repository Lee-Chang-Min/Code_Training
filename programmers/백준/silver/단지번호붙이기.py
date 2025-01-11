from collections import deque

N=int(input())
# # d = [(-1,0), (1,0), (0,-1), (0,1)]
# arr=[list(input()) for _ in range(N)]

# ans = []
# v = [[0]*N for _ in range(N)]

# pop(0) -> O(n)
# pop() -> O(1)


def bfs(si,sj):
    # q = [] #필요 변수 생성
    q = deque()

    q.append((si,sj)) #초기 데이터 삽입
    v[si][sj]=1 # 방문 표시
    cnt = 1  # 정답처리 관련 작업

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni,nj = ci+di, cj+dj

            #4방향 범위내, 미방문 1이면 q 삽입
            if 0 <=ni<N and 0<=nj<N and arr[ni][nj] == '1' and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    return cnt



N = int(input()) # 7
# arr = [list(map(int, input())) for _ in range(N)]
arr = [list(input()) for _ in range(N)]

v = [[0]*N for _ in range(N)]
ans = []
for i in range(N): 
    for j in range(N): 
        # 방문하지 않았던 아파트 발견시 bfs
        if arr[i][j]=='1'and v[i][j]==0:
            ans.append(bfs(i,j))



print(len(ans), *sorted(ans), sep='\n')

























# def dfs(x,y):
#     arr[x][y]='0'
#     cnt=1
#     for i in range(4):
#         nx=x+d[i][0]
#         ny=y+d[i][1]
#         if (0<=nx<N and 0<=ny<N) and arr[nx][ny]=='1':
#             cnt+=dfs(nx,ny)           
#     return cnt



# result=[]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]=='1':
#             result.append(dfs(i,j))            
# print(len(result), *sorted(result), sep='\n')
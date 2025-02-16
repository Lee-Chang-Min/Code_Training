from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni,nj = ci+di,dj+cj
            if 0<ni<N and 0<nj<N and arr[ni][nj] =='1'and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt
                

N = int(input())
arr = [list(input()) for _ in range(N)]

v = [[0]* N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and v[i][j] == '0':
            result.append(bfs(i,j))

print(len(result), *sorted(result), sep='\n')
            
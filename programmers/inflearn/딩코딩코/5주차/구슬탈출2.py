import sys


def move(i,j,dr):
    back = -1
    for cnt in range(1, 10): # 벽을 만날때까지
        ni,nj = i+di[dr]*cnt, j+dj[dr]*cnt
        if arr[ni][nj] == '#': 
            return cnt+back 
        if arr[ni][nj] == 'O': 
            return cnt

        # 다른 공을 지나간 경우 벽을 만났다면 한칸 뒤로
        if arr[ni][nj] == 'B' or arr[ni][nj] == 'R': 
            back -= 1



def dfs(n, ri,rj,bi,bj):
    global ans


    if n > 10: 
        return # 10회 이하까지만 진행

    # 4방향 처리
    for dr in range(4):
        # [1] 각 공의 이동거리 계산
        r_cnt = move(ri,rj,dr) # 해당 방향으로 이동거리
        b_cnt = move(bi,bj,dr)
        if r_cnt == 0 and b_cnt == 0 : # 공이 움직이지 않으니 탐색 종료
            continue
        
        # [2] 각공의 이동 반영
        nri, nrj = ri + di[dr]*r_cnt, rj + dj[dr]*r_cnt
        nbi, nbj = bi + di[dr]*b_cnt, bj + dj[dr]*b_cnt

        #구망에 대한 처리 (빨간색만 들어가면 성공, 파란색이 들어가면 실패)
        #[3] 이동한 위치가 홀인 경우 처리
        if arr[nbi][nbj] == 'O': # 파란색 공이 들어가면 실패
            continue
        else:
            if arr[nri][nrj] == 'O' : # 빨간색 공만
                ans=min(ans, n)
                return
            
        #[4] 둘다 홀이 아닌 경우 (next 좌표 기준으로 다음 시도)
        # 현재 위치를 빈칸, 이동할 위치에 'R', 'B' 구슬 표시
        arr[ri][rj], arr[bi][bj] = '.', '.'
        arr[nri][nrj], arr[nbi][nbj] = 'R', 'B'

        dfs(n+1, nri,nrj,nbi,nbj)

        #원상복구
        arr[nri][nrj], arr[nbi][nbj] = '.', '.' 
        arr[ri][rj], arr[bi][bj] = 'R', 'B'


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# print(arr)
# [['#', '#', '#', '#', '#'], ['#', '.', '.', 'B', '#'], ['#', '.', '#', '.', '#'], ['#', 'R', 'O', '.', '#'], ['#', '#', '#', '#', '#']]


# ri rj bj bj 구슬의 위치
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R' :
            ri, rj = i, j
        if arr[i][j] == 'B' :
            bi, bj = i, j


ans = 11
dfs(1, ri, rj, bi, bj)

if ans == 11 :
    ans = -1

print(ans)
from collections import deque

def find_fastest_time(N, K):
    # 최대 범위 정의
    MAX_POSITION = 100000
    # 방문 시간을 기록하는 리스트(0으로 초기화)
    visited = [0] * (MAX_POSITION + 1)
    
    queue = deque([N])
    while queue:
        current = queue.popleft()
        
        # 동생의 위치에 도달한 경우 현재까지 걸린 시간 반환
        if current == K:
            return visited[current]
        
        # 이동 가능한 위치 확인: current-1, current+1, current*2
        # 범위 체크, 미방문 체크 후 큐에 넣고 방문 시간 기록
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= MAX_POSITION and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 예제 입력
# N, K = map(int, input().split())
print(find_fastest_time(5, 17))

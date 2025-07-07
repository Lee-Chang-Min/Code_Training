from collections import deque

def solution(n, wires):
    # 인접 리스트 
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    

    # BFS 한 덩이의 노드 수 세기
    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            v = q.popleft()
            for nxt in graph[v]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    q.append(nxt)
                    cnt += 1
        return cnt


    best = n                          
    for a, b in wires:
        graph[a].remove(b)            # 전선 끊기
        graph[b].remove(a)

        diff = abs(bfs(a) - bfs(b))   # 두 서브트리 크기 차
        best = min(best, diff)

        graph[a].append(b)            # 전선 복구
        graph[b].append(a)

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
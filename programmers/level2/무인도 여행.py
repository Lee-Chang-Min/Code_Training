from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    islands = []
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        visited[x][y] = True
        total = int(maps[x][y])
        while queue:
            cx,cy = queue.popleft()
            for dx, dy in directions:
                nx,ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total += int(maps[nx][ny])
                    queue.append((nx,ny))
        return total
            
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                food_sum = bfs(i,j)
                islands.append(food_sum)
                
    if not islands:
        return [-1]
    
    return sorted(islands)
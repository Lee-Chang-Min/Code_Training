from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = set()

    while q:
        num, cnt = q.popleft()

        if num > y or num in visited:
            continue
        visited.add(num)
        
        if num == y:
            return cnt

        for k in (num*2, num*3, num+n):
            
            if k <= y and k not in visited:
                q.append((k, cnt + 1))

    return -1
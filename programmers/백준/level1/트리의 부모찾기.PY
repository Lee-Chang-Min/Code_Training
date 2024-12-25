import sys
sys.setrecursionlimit(10**6)


N = int(input())

visited = [0] * (N+1)
tree = [[] for _ in range(N+1)]
answer = [0]*(N+1)

for _ in range(1, N): # 인접 리스트로 저장
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def dfs(number):
    visited[number] = 1
    for i in tree[number]: # 해당 노드에 인접한 노드 중에서
        if visited[i] == 0: # 방문한 적이 없다면
            answer[i] = number
            dfs(i)


dfs(1)

for i in range(2, N+1):
    print(answer[i])
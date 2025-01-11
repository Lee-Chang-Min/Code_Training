
# def dfs(n, lst):
#     if n == M: #M개의 수열 완성
#         ans.append(lst)
#         return
    
#     #하위 단계
#     for j in range(1,N+1):
#         if v[j]==0: #선택하지 않은 숫자인 경우 추가
#             v[j] = 1
#             dfs(n+1, lst+[j])
#             v[j] = 0


# N, M = map(int, input().split())
# ans = []
# v = [0] * (N+1) # 중복확인을 위한 visited[]

# dfs(0,[])

# for a in ans:
#     print(*a)


##풀이 2
######################################

# N, M = map(int, input().split())
# answer = []

# visited = [False]*(N+1)

# def dfs(numbers):
    
#     if len(numbers) == M:
#         answer.append(numbers)
#         return
    
#     for i in range(1,N+1):
#         if not visited[i]:
#             visited[i] = True
#             dfs(numbers+[i])
#             visited[i] = False


# dfs([])

# for ans in answer:
#     for N in ans:
#         print(N,end=" ")
#     print()



##풀이 3
######################################

N,M = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
 



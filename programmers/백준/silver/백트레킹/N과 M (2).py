
N, M = map(int, input().split())


def backtracking(N, M, start , seq):
    if len(seq) == M: # 목표한 길이가 되었으면 return
        print(seq)
        return
    
    for i in range(start, N+1):
        seq.append(i)
        backtracking(N, M, i+1, seq)
        seq.pop()


backtracking(N, M, 1, [])

# for i in range(1, N+1):
#     p


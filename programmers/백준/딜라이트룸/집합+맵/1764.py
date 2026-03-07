import io
import sys

sys.stdin = io.StringIO("""3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
""")
input = sys.stdin.readline

N, M = map(int, input().split())

A = set()
for _ in range(N):
    A.add(input())

B = set()
for _ in range(M):
    B.add(input())

result = 0
answer = []
for a in A:
    if a in B:
        result += 1
        answer.append(a)

answer.sort()
print(result)
for a in answer:
    print(a) 

import io
import sys

import heapq
# 로컬 테스트용 예제 입력
# 제출할 때는 이 부분을 지우거나 주석 처리하세요.
sys.stdin = io.StringIO("""13
0
1
2
0
0
3
2
1
0
0
0
0
0
""")

# input = sys.stdin.readline

import heapq

N = int(input())

# list = []
# for _ in range(N):
#     list.append(int(input()))

# print(list)


heap = []
answer = []
for _ in range(N):
    i = int(input())
    if i == 0:
        if len(heap) == 0:
            answer.append(0)
        else:
            a = -heapq.heappop(heap)
            answer.append(a)
    else:
        heapq.heappush(heap, -i)

print("\n".join(map(str, answer)))

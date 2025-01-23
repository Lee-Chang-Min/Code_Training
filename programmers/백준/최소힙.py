import heapq
import sys
input = sys.stdin.readline

n = int(input())

min_heap = []

for _ in range(n):
    number = int(input())

    if number > 0:
        heapq.heappush(min_heap, number)

    else:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))


import sys

N, K = map(int, input().split())

score = [0] + list(map(int, input().split()))

#누적합 만들기
pre_sum = [0]* (N+1)

for i in range(1,N+1):
    pre_sum[i] = pre_sum[i-1]+score[i]


# print(score)
for _ in range(K):
    start, end = map(int, input().split())
    total = pre_sum[end]-pre_sum[start-1]
    avg = total / (end-start+1)
    print(f'{avg:.2f}')  

    
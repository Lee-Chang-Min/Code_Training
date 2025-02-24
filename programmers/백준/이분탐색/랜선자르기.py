import sys

K, N = map(int, input().split())

lines = []
for _ in range(K):
    lines.append(int(input()))

start, end = 1, max(lines)


while(start <= end):
  
  #만들고 싶은 랜선 길이 => mid
  mid = (start + end) // 2
  line_cnt = 0

  # 가지고 있는 랜선을 돌면서 mid로 나눴을 때 총 몇개로 나눠지는기 계산
  for line in lines:
    line_cnt +=  line // mid 
    # 802 // 401
    
  if line_cnt >= N:
    start = mid + 1
  else:
    end = mid - 1

print(end)


# 목 //, 나머지 %
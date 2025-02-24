import sys

# 총 강의의 수 , 그룹 지을 강의의 수
N, M = map(int, input().split())

time = list(map(int, input().split()))

start = max(time) #블루레이의 가장 작은 사이즈
end = sum(time) # 모든 강의 의 수 보다 큰값이 나올 수 없기때문에 총 합

# print(time)

# answer = 0
# 가능한 블루레이 크기중 최소를 찾아야 함
while start <= end:
    mid = (start + end) // 2

    sum = 0
    count = 1 
    for t in time:
        if sum + t > mid:
            count += 1
            sum = 0 # 초기화
        sum += t

    if count <= M:
        # 중앙값 크기로 모든 레슨을 저장할 수 있으면
        # 종료 인덱스 = 중앙값 - 1
        ans = mid
        end = mid - 1
    else:
        # 중앙값 크기로 모든 레슨을 저장할 수 없으면
        # 시작 인덱스 = 중앙값 + 1
        start = mid + 1
    


print(ans)
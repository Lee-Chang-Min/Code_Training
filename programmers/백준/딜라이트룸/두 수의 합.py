import io
import sys

# 로컬 테스트용 예제 입력
# 제출할 때는 이 부분을 지우거나 주석 처리하세요.
sys.stdin = io.StringIO("""9
5 12 7 10 9 1 2 3 11
13
""")

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
X = int(input())

# 여기에 풀이 작성
# 투 포인터 문제

numbers.sort() # [1, 2, 3, 5, 7, 9, 10, 11, 12]

left = 0
right = N-1
count = 0

while left < right:
    if numbers[left] + numbers[right] == X:
        count += 1
        left += 1
        right -= 1
    elif numbers[left] + numbers[right] < X:
        left += 1
    else:
        right -= 1

print(count) 
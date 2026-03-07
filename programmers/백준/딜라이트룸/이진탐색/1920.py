import io
import sys

# 로컬 테스트용 예제 입력
# 제출할 때는 이 부분을 지우거나 주석 처리하세요.
sys.stdin = io.StringIO("""5
4 1 5 2 3
5
1 3 7 9 5
""")
input = sys.stdin.readline

N = int(input()) 
# numbers = list(input().split()) '4', '1', '5', '2', '3']
numbers = list(map(int,input().split())) 


M = int(input())
targets = list(map(int, input().split()))

# 여기에 풀이 작성
numbers.sort() #[1, 2, 3, 4, 5]

for t in targets: # 1 3 7 9 5

    start = 0
    end = len(numbers)-1 # 4

    while start <= end: 
        mid = (start + end) // 2 # 2
        if numbers[mid] == t:
            print(1)
            break
        elif numbers[mid] < t:
            start = mid + 1
        else:
            end = mid - 1

    if start > end:
        print(0)


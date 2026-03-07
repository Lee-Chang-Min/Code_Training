import io
import sys

# 로컬 테스트용 예제 입력
# 제출할 때는 이 부분을 지우거나 주석 처리하세요.
sys.stdin = io.StringIO("""10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
""")
input = sys.stdin.readline

from collections import Counter

N = input()
card = list(map(int,input().split()))

M = input()
target = list(map(int,input().split()))


# dict = {}

# for c in card:
#     dict[c] = dict.get(c, 0) + 1

# # print(dict)

# for t in target:
#     print(dict.get(t, 0), end=' ')

card = Counter(card)
# print(card)

for t in target:
    print(card.get(t, 0), end=' ')  
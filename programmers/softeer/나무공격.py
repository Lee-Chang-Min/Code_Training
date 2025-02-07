import sys

n,m = map(int, input().split())

격자 = [list(map(int, input().split())) for _ in range(n)]
# 공격범위 = list(map(int,input().split()))
# print(격자)
# print(공격범위)

result = 0

for _ in range(2):
    attack = list(map(int,input().split())) #[1,5]
    for a in range(attack[0]-1, attack[1]): #0~4
        # a = [0,0,1,0,0,0,1,0]
        for i in range(m): # m = 8
            if 격자[a][i] == 1:
                격자[a][i] = 0
                break

for a in 격자:
    cnt = a.count(1)
    result += cnt

print(result)

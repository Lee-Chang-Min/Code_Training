import sys

n = int(input())

난로s = list(map(int, input().split()))
난로s.sort()
res = 0

for i in range(2,max(난로s) + 1): #0 1 2 3 4 5
    cnt = 0
    for j in range(n):
        if 난로s[j] % i == 0 :
            cnt +=1
    res = max(res, cnt)
    

print(res)
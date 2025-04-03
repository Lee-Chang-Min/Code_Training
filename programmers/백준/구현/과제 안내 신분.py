all = []

for i in range(1,31):
    all.append(i)


for _ in range(1, 29):
    re = int(input())
    all.remove(re)


print(f"{all[0]}\n{all[1]}")



######################################
submitted = [False] * 31  # 0~30 (0은 미사용)

for _ in range(28):
    n = int(input())
    submitted[n] = True

for i in range(1, 31):
    if not submitted[i]:
        print(i)



N = int(input())
distance = list(map(int, input().split()))
location_price = list(map(int, input().split()))


result = 0
min_price = location_price[0]

for i in range(0, N - 1):
    min_price = min(min_price, location_price[i])  # 현재까지의 최소 주유 가격 갱신
    result += distance[i] * min_price



print(result)
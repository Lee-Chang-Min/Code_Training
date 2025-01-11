N = int(input())

result_5 = N // 5

# range(start, stop[, step])
for result_5 in range(N//5, -1, -1):
    result_3 = (N-result_5 * 5) // 3

    if result_5 * 5 + result_3 * 3 == N:
        print(result_5 + result_3)
        break
else:
    print(-1)   

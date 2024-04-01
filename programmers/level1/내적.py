def solution(a, b):
    answer = 1234567890
    return answer

a = [1,2,3,4]	
b = [-3,-1,0,2]
answer = 0

for idx in range(len(a)):
    answer += a[idx]*b[idx]

print(answer)
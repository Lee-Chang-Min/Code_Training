def solution(lottos, win_nums):
    answer = []
    return answer

# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]


lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]

result = []
answer = []
등수 = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6,
}
# print(lottos.count(0))
for i in lottos:
    try:
        result.append(win_nums.index(i))
        print(result)
        print(len(result))
    except ValueError:
        continue 

answer.insert(0, next((k for k, v in 등수.items() if v == len(result)+lottos.count(0)), 6))
answer.insert(1,next((k for k, v in 등수.items() if v == len(result)), 6))

print(answer)
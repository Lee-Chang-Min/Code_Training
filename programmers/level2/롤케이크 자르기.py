def solution(topping):
    
    right_num, left_num = [], []
    right_set, left_set = set(), set()

    for idx, top in enumerate(topping):
        right_set.add(top)
        right_num.append(len(right_set))

        left_set.add(topping[len(topping)-idx-1]) 
        left_num.append(len(left_set)) # len(set(topping[idx:]))

    left_num.reverse()
    #answer = [ i for i in range(len(topping)) if right_num[i] == left_num[i] ]
    # answer = []
    # for i in range(len(topping)):
    #     if right_num[i] == left_num[i]:
    #         answer.append(i)
    
    #answer = [i for i in range(len(right_num) - 1) if right_num[i] == left_num[len_left - i - 2]]

    answer = []
    for i in range(len(right_num) - 1):
        if right_num[i] == left_num[i + 1]:
            answer.append(i)

    return len(answer)

solution([1, 2, 1, 3, 1, 4, 1, 2])



# idx = 0 일 때
# 자르는 위치: | 1, 2, 1, 3, 1, 4, 1, 2
# 왼쪽 조각 topping[:0]: []
# set([]) -> {} (종류: 0개)
# 오른쪽 조각 topping[0:]: [1, 2, 1, 3, 1, 4, 1, 2]
# set([1, 2, 1, 3, 1, 4, 1, 2]) -> {1, 2, 3, 4} (종류: 4개)
# 결과: right_num에 0 추가, left_num에 4 추가. (0 != 4)
# idx = 1 일 때
# 자르는 위치: 1 | 2, 1, 3, 1, 4, 1, 2
# 왼쪽 조각 topping[:1]: [1]
# set([1]) -> {1} (종류: 1개)
# 오른쪽 조각 topping[1:]: [2, 1, 3, 1, 4, 1, 2]
# set([2, 1, 3, 1, 4, 1, 2]) -> {1, 2, 3, 4} (종류: 4개)
# 결과: right_num에 1 추가, left_num에 4 추가. (1 != 4)
# idx = 2 일 때
# 자르는 위치: 1, 2 | 1, 3, 1, 4, 1, 2
# 왼쪽 조각 topping[:2]: [1, 2]
# set([1, 2]) -> {1, 2} (종류: 2개)
# 오른쪽 조각 topping[2:]: [1, 3, 1, 4, 1, 2]
# set([1, 3, 1, 4, 1, 2]) -> {1, 2, 3, 4} (종류: 4개)
# 결과: right_num에 2 추가, left_num에 4 추가. (2 != 4)
from collections import deque

c = 11
b = 2

# B -1, B+1, 2 * B


# T 0  1  2  3  4  5 
#  11  12 14 17 21 26

#Brown
# 1 3 4


# 1-1-1 : 0
# 1-1-2 : 2
# 1-1-3 : 1

# 1-2-1 : 2
# 1-2-2 : 4
# 1-2-3 : 6

# 1-3-1 : 3
# 1-3-2 : 5
# 1-3-3 : 8

# 아 이거 모든 경우의 수를 다 봐야 하는 구나 


 
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc,0))
    # print(queue) #deque([(2, 0)])

    v = [{} for _ in range(200001)] # [{},{},{} ... 20만개]

    while cony_loc <= 200000:
        cony_loc += time

        if time in v[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_p, current_t = queue.popleft()

        new_time = current_t + 1

        new_position = current_p - 1
        if 0 <= new_position <=200000:
            v[new_position][new_time] = True
            queue.append(new_position, new_time) # brown_loc - 1 , 1
        new_position = brown_loc + 1
        if 0 <= new_position <=200000:
            v[new_position][new_time] = True
            queue.append(new_position, new_time) 
        new_position = brown_loc * 2
        if 0 <= new_position <=200000:
            v[new_position][new_time] = True
            queue.append(new_position, new_time) 

    time += 1
    
    return


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
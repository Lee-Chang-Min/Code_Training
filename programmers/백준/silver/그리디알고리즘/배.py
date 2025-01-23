import sys

crane_cnt = int(input())
crane = list(map(int, input().split()))

box_cnt = int(input())
box = list(map(int, input().split()))


crane.sort(reverse=True) #[9,8,6]
box.sort(reverse=True) #[7,5,4,2,2]

time = 0

if(crane[0] < box[0]):
    print(-1)
    sys.exit()
else:

    while len(box) > 0: # 박스가 모두 옮겨질때 까지 반복

        for c in crane:
            if box and c < box[-1]: # 해당 과정을 거치지 않으면 시간 초과
                # if c < box[-1]:    
                continue
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        time += 1


print(time)


# 우선순위 큐
def solution(plans):
    stack = []
    answer = []

#시간을 int로 바꾼다 
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':')) 
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]

        while stack and gap:
            nowTime = stack[-1][1] 
            
            if nowTime <= gap: 
                name, time = stack.pop() 
                gap -= time 
                answer.append(name) 
            else: 
                nowTime -= gap 
                gap = 0 # 다음과제 해야하니까 0

    answer.append(plans[-1][0])

    for i in range(len(stack)):
        answer.append(stack[~i][0])  

    return answer


print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
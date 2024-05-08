def solution(n):
    answer = []

    while(n>2):
        # print(f'n: {n}')
        # print(f'n%3: {int(n%3)}')
        # answer.append(n % 3)
        
        if(int(n%3) == 2 or int(n%3) == 1 ):
            answer.append(int(n%3))
            answer.append(int(n//3))
            break;
        elif(int(n%3) == 0):
            answer.append(0)
        n = n/3

    answer.reverse()
    vals = 0
    for idx, val in enumerate(answer):
        # print(3**idx)
        vals += val * 3**idx
    return vals

n = 125
answer = []

while(n>2):
    print(f'n: {n}')
    print(f'n%3: {int(n%3)}')
    # answer.append(n % 3)
    
    if(int(n%3) == 2 or int(n%3) == 1 ):
        answer.append(int(n%3))
        answer.append(int(n//3))
        break;
    elif(int(n%3) == 0):
        answer.append(0)
    n = n/3

answer.reverse()
vals = 0
print(answer)
for idx, val in enumerate(answer):
    # print(3**idx)
    vals += val * 3**idx
    
print(vals)
import sys

N = int(input().strip()) 

fruit_num = list(map(int, input().split()))
# [5, 1, 1, 2, 1]

left = 0
max_len = 0 # 최대 길이 저장 탐색하면서 계속 갱신
fruit_dic = {} #{5: 1, 1:2}

for right in range(N):
    current_fruit = fruit_num[right]
    
    #현재 과일을 fruit_dic 에 저장
    if current_fruit in fruit_dic:
        fruit_dic[current_fruit] += 1 # {5: 1, 1: 2. 2:1}
    else:
        fruit_dic[current_fruit] = 1
    
    while len(fruit_dic) > 2:
        fruit_to_remove = fruit_num[left] 
        
        fruit_dic[fruit_to_remove] -= 1 # { 1: 2, 2:1}
        
        if fruit_dic[fruit_to_remove] == 0:
            del fruit_dic[fruit_to_remove]
        
        left += 1
    
    max_len = max(max_len, right - left + 1) # 2

print(max_len)
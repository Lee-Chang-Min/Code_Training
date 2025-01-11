

def minimize_expression(expression):
    # "-"로 식을 나눔
    parts = expression.split('-')
    
    # 각 부분에 "+" 계산 수행
    sums = []
    for part in parts:
        # 예시 ["10+20+30", "40+50", "60"]


        # "+"로 나누어 각 블록의 합 계산
        numbers = map(int, part.split('+'))
        sums.append(sum(numbers))
    
    # 첫 번째 블록은 더하고, 나머지는 모두 뺌
    result = sums[0]
    for s in sums[1:]:
        result -= s
    
    return result

# 입력 처리 및 함수 호출
expression = input()
print(minimize_expression(expression))

#아이디어
#첫번째 => - 기준으로 일단 다 자르고 

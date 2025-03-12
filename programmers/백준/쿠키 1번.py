
jelly = [100,50,5,1]

def solution(score):
    answer = 0

    for j in jelly:
        answer += score // j # 3 임
        score = score % j #나머지

    return answer


solution(319)
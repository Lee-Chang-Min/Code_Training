

def solution(pouches):

    # 특정맛 젤리를 가장 많이 선택해야함
    # 주머니에 특정맛이 얼마나 많이 들어있는지 봐야함
    answer = 0
    jelly = ['a', 'b', 'c', 'd', 'e']

    for j in jelly:
        score = []

        # 각 파우치별 다른 젤리에 비해 얼마나 있는지
        for p in pouches:
            cnt_choice = p.count(j)
            cnt_total = len(p)
            cnt_other = cnt_total - cnt_choice
            rest = cnt_choice - cnt_other
            score.append(rest)

        score.sort(reverse=True)

        select = 0 # 선택한 주머니 수
        total_rest = 0

        #각 젤리면 점수를 보면서 선택할지말지 고름
        for s in score:
            total_rest += s

            if total_rest > 0:
                select += 1
            else:
                #음수면 추가할 필요가 없음
                break 

        if select > answer:
            answer = select
        
    return answer

# 테스트 예시
print(solution(["cab", "adaaa", "e"]))         # 출력: 3
# print(sol(["aabb", "baba"]))               # 출력: 0
# print(sol(["a"]))                         # 출력: 1
# print(sol(["d", "a", "e", "d", "abdcc"]))   # 출력: 3

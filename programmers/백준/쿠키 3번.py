# def sol(pouches):
#     flavors = ['a', 'b', 'c', 'd', 'e']
#     max_selected = 0  # 모든 맛 중 선택 가능한 최대 주머니 수

#     # 각 맛에 대해 반복
#     for f in flavors:
#         contributions = []  # 각 주머니가 해당 맛을 얼마나 돋보이게 하는지 저장할 리스트

#         # 각 주머니에 대해 해당 맛의 젤리 개수와 다른 맛의 젤리 개수를 계산
#         for pouch in pouches:
#             count_chosen = pouch.count(f)       # 주머니에서 맛 f의 젤리 개수
#             count_total = len(pouch)              # 주머니의 전체 젤리 개수
#             count_others = count_total - count_chosen  # 주머니에서 다른 맛의 젤리 개수
#             # '초과분'은 맛 f의 젤리 개수에서 다른 맛 젤리 개수를 뺀 값입니다.
#             # 이 값이 클수록 그 주머니는 맛 f를 돋보이게 합니다.
#             excess = count_chosen - count_others
#             contributions.append(excess)

#         # 가장 많이 기여하는 주머니부터 선택하기 위해 내림차순 정렬
#         contributions.sort(reverse=True)

#         total_excess = 0  # 선택한 주머니들의 '초과분' 누적합
#         selected = 0      # 선택한 주머니의 수

#         # 내림차순으로 정렬된 주머니들을 하나씩 선택하면서 누적 '초과분'을 구합니다.
#         for value in contributions:
#             total_excess += value
#             # 누적 '초과분'이 양수이면, 전체적으로 맛 f의 젤리 개수가 다른 젤리 개수보다 많은 상태입니다.
#             if total_excess > 0:
#                 selected += 1
#             else:
#                 # 누적 '초과분'이 0 이하가 되면 더 이상 주머니를 추가하면 조건이 깨지므로 종료합니다.
#                 break

#         # 현재 맛 f로 선택한 주머니 수와 지금까지의 최대값을 비교하여 업데이트합니다.
#         if selected > max_selected:
#             max_selected = selected

#     return max_selected

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

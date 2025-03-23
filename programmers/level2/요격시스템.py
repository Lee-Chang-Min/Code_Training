def solution(targets):
    targets.sort()
    # print(targets)
    
    answer, end = 0,0
    for s, e in targets:
        if s < end :
            end = min(e,end)
            continue
        else:
            answer += 1
            end = e
    return answer
    

print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))
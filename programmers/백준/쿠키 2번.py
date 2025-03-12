def solution(capacity, routes):
    answer = True

    #from에 도착하면 선물을 더하기
    #to에 도착하면 선물을 빼기

    gift_array = []

    for gift, f, t in routes:
        gift_array.append((f ,gift))
        gift_array.append((t ,-gift))

    # print(gift_array)
    # [(2, 3), (6, -3), (1, 5), (4, -5), (7, 1), (13, -1)]

    # 정렬 한다면? 정렬할때 뺄 선물이 먼저 와야함 
    gift_array.sort(key=lambda x: (x[0], x[1]))
    print(gift_array)
    

    current = 0
    for i, g in gift_array:
        # print(i,g)
        current += g # 선물을 더해나감
        if current > capacity:
            answer = False
            return answer 


    return answer


# solution(8, [[3, 12, 16], [8, 2, 12], [1, 14, 15]])
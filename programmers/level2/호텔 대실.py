import heapq

def time_to_minutes(time_str):
    hh, mm = map(int, time_str.split(':'))
    return hh * 60 + mm


def solution(book_time: list) -> int:

    answer = 0 # 코니에게 필요한 최소 객실의 수

    book_time.sort(key=lambda x: x[0])
    heap = []

    for start, end in book_time:
        # ["15:00", "17:00"]
        start_time = time_to_minutes(start) 
        end_time = time_to_minutes(end) + 10 # 청소 시간 10분 추가 

        # 힙이 비어있지 않으면(사용할 객실이 있을 수 있음) 가장 빨리 퇴실하는 객실의 퇴실 시각 확인
        if heap and start_time >= heap[0]:
            heapq.heappop(heap) # 사용 가능한 객실이므로 pop
        else: 
            answer += 1 # 새로운 객실 필요

        heapq.heappush(heap, end_time) 

    return answer

# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
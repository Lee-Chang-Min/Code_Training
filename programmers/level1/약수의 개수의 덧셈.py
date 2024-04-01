

def solution(left, right):
    answer = 0

    for key in range(left, right+1):
        count = 0
        
        for i in range(1, key + 1):
            if (key % i == 0) :

                count += 1
        print(count / 2) 
        answer += key if count % 2 == 0 else -key

    return answer

        
        


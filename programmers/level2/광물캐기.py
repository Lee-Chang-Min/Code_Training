
chart = [[1,1,1],[5,1,1],[25,5,1]]

def solution(picks, minerals):
    answer = 0
    
    # 다이아 곡갱이를 우선적으로 소모 
    dia = picks[0]
    iron = picks[1]
    stone = picks[2]
    
    곡갱이 = 0
    for m in minerals:
        if (dia != 0):
            if 곡갱이 == 5: 
                dia -= 1 
                곡갱이 = 0
            else:
                곡갱이 += 1
                answer += 1
        
        elif (dia == 0 and iron != 0):
            if 곡갱이 == 5: 
                iron -= 1 
                곡갱이 = 0
            else:   
                if (m == "diamond"):
                    곡갱이 += 1
                    answer += 5  
                else:
                    곡갱이 += 1
                    answer += 1  
        
        # else:
        #     if 곡갱이 == 5: 
        #         stone -= 1 
        #         곡갱이 = 0
        #     else:   
        #         if (m == "diamond"):
        #             곡갱이 += 1
        #             answer += 25  
        #         elif (m == "iron"):
        #             곡갱이 += 1
        #             answer += 5 
        #         elif (m == "stone"):
        #             곡갱이 += 1
        #             answer += 1

                
    

    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
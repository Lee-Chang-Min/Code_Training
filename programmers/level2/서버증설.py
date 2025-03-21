# server= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# server = [k] * 24 

def solution(players, m, k):
    server = [m] * 24 
    count = 0
    for idx, player in enumerate(players):
        # print(idx, p)
        if (player >= server[idx]): # 서버 증설이 필요함

            #몇 대 서버 증설이 필요한지 
            증설 = (( player - server[idx] ) // m) + 1
            # if ( player - server[idx] ) % m == 0:    # 몫을 구해야함
            #     증설 = ( player - server[idx] ) // m  
            # else:
            #     증설 = (( player - server[idx] ) // m) + 1

            count += 증설
            for i in range(idx, idx+k): #서버가 켜져 있는 것 기록 
                server[i] += (m*증설) 
            
    return count



print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))

# 11
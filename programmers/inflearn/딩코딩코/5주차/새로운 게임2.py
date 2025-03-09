


k = 4  # 말의 개수

# 0은 흰색, 1은 빨간색, 2는 파란색
chess = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 동 서 북 남
# →, ←, ↑, ↓
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def goback(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


# 아 이거 쌓인 순서를 지정 해야함 -> 맵에서 어떻게 체스 말들이 쌓여져 있는지 저장해야 됨
# 쌓인 순서대로 같이 이동 -> stack
# 턴 한번은 1번 말부터 K번 말까지 순서대로 이동 -> 반복문을 통해 각 말을 이동 시키는 것이 필요

#말의 현재 위치
# current = [
#     [[0],[1],[2],0],
#     [0,0,0,0],
#     [0,0,[3],0],
#     [0,0,0,0]
# ]


def getgameover (horse_count, game_map, horse_loc):
    n = len(game_map)
    turn_count = 1
    print("n =",n)

    current = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_loc[i]
        current[r][c].append(i)
    # print(current)
    
    while turn_count <=1000:
        for horse_index in range(horse_count): #horse_index 는 몇번째 말인지
            r, c, d = horse_loc[horse_index]

            new_r, new_c = r + dr[d], c+dc[d]

            #파란색의 경우
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = goback(d)

                # 이동방향을 반대로 하고 한칸 이동, 방향을 바꾼 후 이동하려는 칸이 파란색인 경우는 이동하지 않고 가만히 있는다.
                new_r, new_c = r+dr[new_d], c+dc[new_d]
                horse_loc[horse_index][2] = new_d

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue



            # 흰색의 경우 칸 이동, 이동한 칸에 말이 있는 경우 가장 위에 나의 말을 올려놓음
            # 말을 같이 이동함
            # 추가로 1,2,3 이 쌓여있고 이동하려는 칸에 4,5가 있는경우 4,5,1,2,3

            moving_horse = []
            for i in range(len(current[r][c])):
                current_index = current[r][c][i]  

                if horse_index == current_index:
                    moving_horse = current[r][c][i:]
                    current[r][c] = current[r][c][:i] # 말이 이동했으니 원래 위치에서는 지워 줘야 함
                    break
                
                # 빨간색인 경우에는 이동한 후 이동한 말에 대해 모든 말의 쌓여있는 순서를 바꾼다 
            if game_map[new_r][new_c] == 1:
                moving_horse = reversed(moving_horse) 

            
            #이제 새로운 곳에 말을 넣어주면 됌
            for moving_horse_i in moving_horse:
                current[new_r][new_c].append(moving_horse_i)
                horse_loc[moving_horse_i][0], horse_loc[moving_horse_i][1] = new_r, new_c #말의 위치가 이동했으니 업데이트 

            if len(current[new_r][new_c]) >=4:
                return turn_count
        
        turn_count +=1


    return -1


# print(getgameover(k,chess,start_horse))


start_horse = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", getgameover(k, chess, start_horse))


###############################
# n = 3
# [[[] for _ in range(n)] for _ in range(n)]
